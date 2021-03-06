"""
Classes from the 'UIKit' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


_UITargetedProxy = _Class("_UITargetedProxy")
_UIViewServiceUIBehaviorProxy = _Class("_UIViewServiceUIBehaviorProxy")
_UIViewServiceReplyControlTrampoline = _Class("_UIViewServiceReplyControlTrampoline")
_UIViewServiceReplyAwaitingTrampoline = _Class("_UIViewServiceReplyAwaitingTrampoline")
_UIViewServiceImplicitAnimationDecodingProxy = _Class(
    "_UIViewServiceImplicitAnimationDecodingProxy"
)
_UIViewServiceViewControllerDeputy = _Class("_UIViewServiceViewControllerDeputy")
_UIQueueingProxy = _Class("_UIQueueingProxy")
_UIViewServiceFencingControlProxy = _Class("_UIViewServiceFencingControlProxy")
_UIUserNotificationRestrictedAlertViewProxy = _Class(
    "_UIUserNotificationRestrictedAlertViewProxy"
)
_UIUserNotificationAlertViewRestrictedTextField = _Class(
    "_UIUserNotificationAlertViewRestrictedTextField"
)
_UIViewServiceImplicitAnimationEncodingProxy = _Class(
    "_UIViewServiceImplicitAnimationEncodingProxy"
)
_UIViewControllerControlMessageDeputy = _Class("_UIViewControllerControlMessageDeputy")
_UIDiffableDataSourceItemRenderer = _Class("_UIDiffableDataSourceItemRenderer")
_UIOutlineItemRenderer = _Class("_UIOutlineItemRenderer")
_UIOutlineItemRendererInternal = _Class("_UIOutlineItemRendererInternal")
_UIDiffableDataSourceItemRendererInternal = _Class(
    "_UIDiffableDataSourceItemRendererInternal"
)
_UIDatePickerDataModel = _Class("_UIDatePickerDataModel")
_UIPassthroughScrollInteraction = _Class("_UIPassthroughScrollInteraction")
_UITreeDataSourceSnapshotter = _Class("_UITreeDataSourceSnapshotter")
_UISliderControlStateContent = _Class("_UISliderControlStateContent")
_UISliderDataModel = _Class("_UISliderDataModel")
UISceneActivationRequestOptions = _Class("UISceneActivationRequestOptions")
UISceneOpenExternalURLOptions = _Class("UISceneOpenExternalURLOptions")
UISceneOpenURLOptions = _Class("UISceneOpenURLOptions")
UICollectionViewDiffableDataSourceReorderingHandlers = _Class(
    "UICollectionViewDiffableDataSourceReorderingHandlers"
)
_UIShareParticipantDetails = _Class("_UIShareParticipantDetails")
_UISharingControllerActivityItemSource = _Class(
    "_UISharingControllerActivityItemSource"
)
_UIWebViewportHandler = _Class("_UIWebViewportHandler")
UIWebPaginationInfo = _Class("UIWebPaginationInfo")
UIWebOverflowScrollListener = _Class("UIWebOverflowScrollListener")
UIWebGeolocationPolicyDecider = _Class("UIWebGeolocationPolicyDecider")
_UIWebGeolocationChallengeData = _Class("_UIWebGeolocationChallengeData")
UIWebViewWebViewDelegate = _Class("UIWebViewWebViewDelegate")
_UIWebViewScrollViewDelegateForwarder = _Class("_UIWebViewScrollViewDelegateForwarder")
UIWebViewInternal = _Class("UIWebViewInternal")
_UIColorPickerViewControllerConfiguration = _Class(
    "_UIColorPickerViewControllerConfiguration"
)
UIWebURLAction = _Class("UIWebURLAction")
_UIContextMenuAnimator = _Class("_UIContextMenuAnimator")
UIWebPDFSearchController = _Class("UIWebPDFSearchController")
UIWebPDFSearchResult = _Class("UIWebPDFSearchResult")
UIWebPDFViewHandler = _Class("UIWebPDFViewHandler")
UIWebPDFLinkAction = _Class("UIWebPDFLinkAction")
_UICollectionViewLayoutInteractionStateModule = _Class(
    "_UICollectionViewLayoutInteractionStateModule"
)
UIWebElementAction = _Class("UIWebElementAction")
UIWebElementActionInfo = _Class("UIWebElementActionInfo")
UIListContentImageProperties = _Class("UIListContentImageProperties")
UIWebClip = _Class("UIWebClip")
UIWebClipLinkTag = _Class("UIWebClipLinkTag")
UIWebClipIcon = _Class("UIWebClipIcon")
UIWebOverflowScrollInfo = _Class("UIWebOverflowScrollInfo")
UIWebOverflowScrollViewInfo = _Class("UIWebOverflowScrollViewInfo")
UIThreadSafeNode = _Class("UIThreadSafeNode")
UIFocusRingStyle = _Class("UIFocusRingStyle")
UIWebBrowserFindOnPageHighlighter = _Class("UIWebBrowserFindOnPageHighlighter")
_UIViewLFLDChangeRecord = _Class("_UIViewLFLDChangeRecord")
_UIViewLFLDVariableChangeRecord = _Class("_UIViewLFLDVariableChangeRecord")
_UIViewLFLDGeometryChangeRecord = _Class("_UIViewLFLDGeometryChangeRecord")
_UIStackedImageSingleNamedStack = _Class("_UIStackedImageSingleNamedStack")
_UIStackedImageSingleNamedLayerImage = _Class("_UIStackedImageSingleNamedLayerImage")
_UIStackedImageSimpleImage = _Class("_UIStackedImageSimpleImage")
_UIStackedImageConfiguration = _Class("_UIStackedImageConfiguration")
_UIDragSetDownItemAnimation = _Class("_UIDragSetDownItemAnimation")
_UIPopoverViewArtworkLoader = _Class("_UIPopoverViewArtworkLoader")
_UIDragPreviewBlockProvider = _Class("_UIDragPreviewBlockProvider")
_UIDatePickerCalendarTimeValueStore = _Class("_UIDatePickerCalendarTimeValueStore")
_UIContentUnavailableViewCacheKey = _Class("_UIContentUnavailableViewCacheKey")
_UIViewKeyValueAnimationFactory = _Class("_UIViewKeyValueAnimationFactory")
_UIViewKeyValueAnimationFactoryTransition = _Class(
    "_UIViewKeyValueAnimationFactoryTransition"
)
_UIDatePickerCalendarDaySet = _Class("_UIDatePickerCalendarDaySet")
_UIViewCALayerKeyValueMapper = _Class("_UIViewCALayerKeyValueMapper")
_UIViewAnimationDelegate = _Class("_UIViewAnimationDelegate")
UIViewAnimationInfo = _Class("UIViewAnimationInfo")
_UIViewMaskViewWrapper = _Class("_UIViewMaskViewWrapper")
_UIViewDeferredAnimation = _Class("_UIViewDeferredAnimation")
_UIViewDeferredKeyframeAnimation = _Class("_UIViewDeferredKeyframeAnimation")
_UIViewDeferredBasicAnimation = _Class("_UIViewDeferredBasicAnimation")
_UIViewAnimationFrame = _Class("_UIViewAnimationFrame")
_UIViewWeakCAAnimationDelegate = _Class("_UIViewWeakCAAnimationDelegate")
UIViewBlockBasedCAAction = _Class("UIViewBlockBasedCAAction")
_UIImageViewPretiledImageWrapper = _Class("_UIImageViewPretiledImageWrapper")
_UIImageViewPretiledImageCacheKey = _Class("_UIImageViewPretiledImageCacheKey")
_UIScrollDynamics = _Class("_UIScrollDynamics")
_UIScrollDynamicsiOSMac = _Class("_UIScrollDynamicsiOSMac")
_UIScrollViewSimulatedGesture = _Class("_UIScrollViewSimulatedGesture")
_UIScrollViewGestureSimulator = _Class("_UIScrollViewGestureSimulator")
_UIScrollViewMockPinchGestureRecognizer = _Class(
    "_UIScrollViewMockPinchGestureRecognizer"
)
_UIScrollViewMockPanGestureRecognizer = _Class("_UIScrollViewMockPanGestureRecognizer")
UIScrollTestParameters = _Class("UIScrollTestParameters")
_UIDiffableDataSourceUpdate = _Class("_UIDiffableDataSourceUpdate")
_UIDiffableDataSourceState = _Class("_UIDiffableDataSourceState")
UIIndexBarVisualStyle_Base = _Class("UIIndexBarVisualStyle_Base")
UIIndexBarVisualStyle_LegacyiOS = _Class("UIIndexBarVisualStyle_LegacyiOS")
UIIndexBarEntry = _Class("UIIndexBarEntry")
UIIndexBarDisplayEntry = _Class("UIIndexBarDisplayEntry")
UIIndexBarDisplayEntry_LegacyIOS = _Class("UIIndexBarDisplayEntry_LegacyIOS")
_UIVectorTextLayoutGlyph = _Class("_UIVectorTextLayoutGlyph")
_UIVectorTextLayoutRun = _Class("_UIVectorTextLayoutRun")
_UIVectorTextLayoutParameters = _Class("_UIVectorTextLayoutParameters")
_UIVectorTextLayout = _Class("_UIVectorTextLayout")
_UIVectorTextLayoutInfo = _Class("_UIVectorTextLayoutInfo")
_UICollectionViewCompositionalLayoutMutableConfiguration = _Class(
    "_UICollectionViewCompositionalLayoutMutableConfiguration"
)
_UICollectionLayoutAnchor = _Class("_UICollectionLayoutAnchor")
_UICollectionLayoutEdgeSpacing = _Class("_UICollectionLayoutEdgeSpacing")
_UICollectionLayoutSpacing = _Class("_UICollectionLayoutSpacing")
_UICollectionLayoutSize = _Class("_UICollectionLayoutSize")
_UICollectionLayoutDimension = _Class("_UICollectionLayoutDimension")
_UICollectionLayoutItem = _Class("_UICollectionLayoutItem")
_UICollectionLayoutDecorationItem = _Class("_UICollectionLayoutDecorationItem")
_UICollectionLayoutSupplementaryItem = _Class("_UICollectionLayoutSupplementaryItem")
_UICollectionLayoutBoundarySupplementaryItem = _Class(
    "_UICollectionLayoutBoundarySupplementaryItem"
)
_UICollectionLayoutGroup = _Class("_UICollectionLayoutGroup")
_UICollectionLayoutSection = _Class("_UICollectionLayoutSection")
_UILabelScaledMetrics = _Class("_UILabelScaledMetrics")
_UIViewAnimationWithComposerWrapper = _Class("_UIViewAnimationWithComposerWrapper")
_UICGImageDecompressor = _Class("_UICGImageDecompressor")
UIViewInProcessAnimationManager = _Class("UIViewInProcessAnimationManager")
UIViewAnimationComposer = _Class("UIViewAnimationComposer")
UIViewRunningAnimationEntry = _Class("UIViewRunningAnimationEntry")
UIInterpolatedValue = _Class("UIInterpolatedValue")
UIInterpolatedTransform = _Class("UIInterpolatedTransform")
UIInterpolatedSize = _Class("UIInterpolatedSize")
UIInterpolatedRect = _Class("UIInterpolatedRect")
UIInterpolatedNormalizedRect = _Class("UIInterpolatedNormalizedRect")
UIInterpolatedPoint = _Class("UIInterpolatedPoint")
UIInterpolatedNormalizedPoint = _Class("UIInterpolatedNormalizedPoint")
UIInterpolatedFloat = _Class("UIInterpolatedFloat")
UIInterpolatedScaledFloat = _Class("UIInterpolatedScaledFloat")
UIInterpolatedColor = _Class("UIInterpolatedColor")
UIViewUpdateVelocityAnimationDescription = _Class(
    "UIViewUpdateVelocityAnimationDescription"
)
UIViewRetargetingAnimationDescription = _Class("UIViewRetargetingAnimationDescription")
UIViewInstaneouslyStableAnimation = _Class("UIViewInstaneouslyStableAnimation")
UIViewFrictionBounceAnimation = _Class("UIViewFrictionBounceAnimation")
UIViewSpringAnimationDescription = _Class("UIViewSpringAnimationDescription")
UIViewSpringAnimationBehavior = _Class("UIViewSpringAnimationBehavior")
UIViewSpringAnimation = _Class("UIViewSpringAnimation")
UIFloatSpringIntegrator = _Class("UIFloatSpringIntegrator")
UIFloatCompoundSpringIntegrator = _Class("UIFloatCompoundSpringIntegrator")
_UIViewPropertyInfo = _Class("_UIViewPropertyInfo")
_UIPreviewInteractionPresentationAssistant = _Class(
    "_UIPreviewInteractionPresentationAssistant"
)
_UIViewAnimatablePropertyTransformer = _Class("_UIViewAnimatablePropertyTransformer")
UIAnimatablePropertyBase = _Class("UIAnimatablePropertyBase")
UIViewFloatAnimatableProperty = _Class("UIViewFloatAnimatableProperty")
UIViewProgressAnimatableProperty = _Class("UIViewProgressAnimatableProperty")
UIAnimatableProperty = _Class("UIAnimatableProperty")
_UIRadiosityImageGenerator = _Class("_UIRadiosityImageGenerator")
_UIViewBaselineLoweringInfo = _Class("_UIViewBaselineLoweringInfo")
_NSLayoutConstraintConstant = _Class("_NSLayoutConstraintConstant")
_UIFulfilledContextMenuConfiguration = _Class("_UIFulfilledContextMenuConfiguration")
UIContextMenuConfiguration = _Class("UIContextMenuConfiguration")
_UIStatusBarStateStackInfo = _Class("_UIStatusBarStateStackInfo")
UIInterpolatedColorMatrix = _Class("UIInterpolatedColorMatrix")
_UIViewServiceSession = _Class("_UIViewServiceSession")
_UICollectionViewListLayoutSectionConfiguration = _Class(
    "_UICollectionViewListLayoutSectionConfiguration"
)
_UICollectionViewEnvironmentAdapter = _Class("_UICollectionViewEnvironmentAdapter")
_UISunScheduleController = _Class("_UISunScheduleController")
_UIPreview = _Class("_UIPreview")
_UIVibrantSettings = _Class("_UIVibrantSettings")
_UIPopoverLayoutInfo = _Class("_UIPopoverLayoutInfo")
_UISlidingPopoverLayoutInfo = _Class("_UISlidingPopoverLayoutInfo")
_UICubicPolyTangent = _Class("_UICubicPolyTangent")
_UIAutologgingDeallocSentinel = _Class("_UIAutologgingDeallocSentinel")
_UILazyMapTable = _Class("_UILazyMapTable")
_UIAssociationTable = _Class("_UIAssociationTable")
UIPointerInteractionAnimator = _Class("UIPointerInteractionAnimator")
_UIPrototypingValue = _Class("_UIPrototypingValue")
_UIPrototypingSettingsManager = _Class("_UIPrototypingSettingsManager")
UIDebuggingIvar = _Class("UIDebuggingIvar")
_UIDebuggingOverlayDetail = _Class("_UIDebuggingOverlayDetail")
_UIDebuggingOverlayDetailOpacity = _Class("_UIDebuggingOverlayDetailOpacity")
_UIDebuggingOverlayViewControllerDetail = _Class(
    "_UIDebuggingOverlayViewControllerDetail"
)
_UIDebuggingOverlayDetailIvar = _Class("_UIDebuggingOverlayDetailIvar")
_UIDebuggingOverlayPresentingViewControllerDetail = _Class(
    "_UIDebuggingOverlayPresentingViewControllerDetail"
)
_UIDebuggingOverlayPresentedViewControllerDetail = _Class(
    "_UIDebuggingOverlayPresentedViewControllerDetail"
)
_UIDebuggingOverlayViewDetail = _Class("_UIDebuggingOverlayViewDetail")
UIDebuggingInformationVCHierarchyDataContainer = _Class(
    "UIDebuggingInformationVCHierarchyDataContainer"
)
UIDebuggingInformationHierarchyDataContainer = _Class(
    "UIDebuggingInformationHierarchyDataContainer"
)
UIDebuggingInformationOverlayInvokeGestureHandler = _Class(
    "UIDebuggingInformationOverlayInvokeGestureHandler"
)
UIDraggingSystemSceneMetadata = _Class("UIDraggingSystemSceneMetadata")
UIDraggingSystemMonitor = _Class("UIDraggingSystemMonitor")
UIDraggingSystemSession = _Class("UIDraggingSystemSession")
UIDraggingSystemSessionInfo = _Class("UIDraggingSystemSessionInfo")
UIDraggingSystemTouchRoutingPolicy = _Class("UIDraggingSystemTouchRoutingPolicy")
_UITextItem = _Class("_UITextItem")
_UITextItemDiscoverer = _Class("_UITextItemDiscoverer")
UIFontPickerController = _Class("UIFontPickerController")
_UIBoundingTextRectsSolver = _Class("_UIBoundingTextRectsSolver")
UIInputContextHistory = _Class("UIInputContextHistory")
UITextCheckerDictionaryEntry = _Class("UITextCheckerDictionaryEntry")
_UIGestureStudyInteraction = _Class("_UIGestureStudyInteraction")
_UICharacterStreamingManager = _Class("_UICharacterStreamingManager")
_UISelectorSet = _Class("_UISelectorSet")
_UIFocusGroupMap = _Class("_UIFocusGroupMap")
_UITextAttachmentViewHelper = _Class("_UITextAttachmentViewHelper")
UITextPlaceholder = _Class("UITextPlaceholder")
UIWebTextPlaceholder = _Class("UIWebTextPlaceholder")
_UITextFieldBackgroundCacheKey = _Class("_UITextFieldBackgroundCacheKey")
_UITextFieldClearButtonCacheKey = _Class("_UITextFieldClearButtonCacheKey")
_UITextFieldEditingToken = _Class("_UITextFieldEditingToken")
_UITextFieldEditingProcessor = _Class("_UITextFieldEditingProcessor")
_UIForceClickInteractionDriver = _Class("_UIForceClickInteractionDriver")
_UICompatibilityForceClickInteractionDriver = _Class(
    "_UICompatibilityForceClickInteractionDriver"
)
_UIDatePickerCalendarDateComponent = _Class("_UIDatePickerCalendarDateComponent")
_UIDatePickerCalendarTime = _Class("_UIDatePickerCalendarTime")
_UIDatePickerCalendarMonth = _Class("_UIDatePickerCalendarMonth")
_UIDatePickerCalendarDay = _Class("_UIDatePickerCalendarDay")
_UITextTiledLayerMaskedRect = _Class("_UITextTiledLayerMaskedRect")
UIWebSelectionGraph = _Class("UIWebSelectionGraph")
UIWebSelectionNode = _Class("UIWebSelectionNode")
_UICommandDiffv1 = _Class("_UICommandDiffv1")
_UICommandChange = _Class("_UICommandChange")
_UICommandMenuInsertion = _Class("_UICommandMenuInsertion")
_UICommandMenuDeletion = _Class("_UICommandMenuDeletion")
_UICommandItemInsertion = _Class("_UICommandItemInsertion")
_UICommandItemDeletion = _Class("_UICommandItemDeletion")
_UIDatePickerDateRange = _Class("_UIDatePickerDateRange")
UIWebSelectionAssistant = _Class("UIWebSelectionAssistant")
UIWebSelection = _Class("UIWebSelection")
_UIImageSystemImageVisualStyle = _Class("_UIImageSystemImageVisualStyle")
UIWKAutocorrectionRects = _Class("UIWKAutocorrectionRects")
UIWKAutocorrectionContext = _Class("UIWKAutocorrectionContext")
UIWKDocumentRequest = _Class("UIWKDocumentRequest")
UIWKDocumentContext = _Class("UIWKDocumentContext")
UITextTouchObservingInteraction = _Class("UITextTouchObservingInteraction")
UITextSelectionGrabberSuppressionAssertion = _Class(
    "UITextSelectionGrabberSuppressionAssertion"
)
UITextReplacementGenerator = _Class("UITextReplacementGenerator")
UITextReplacementGeneratorForMultilingualDictation = _Class(
    "UITextReplacementGeneratorForMultilingualDictation"
)
UITextReplacementGeneratorForDictation = _Class(
    "UITextReplacementGeneratorForDictation"
)
UITextReplacementGeneratorForChineseTransliteration = _Class(
    "UITextReplacementGeneratorForChineseTransliteration"
)
UITextReplacementGeneratorForCorrections = _Class(
    "UITextReplacementGeneratorForCorrections"
)
UITextReplacement = _Class("UITextReplacement")
_UICarPlaySceneComponent = _Class("_UICarPlaySceneComponent")
_UITextLinkInteractionSession = _Class("_UITextLinkInteractionSession")
UITextInteractionInputDelegate = _Class("UITextInteractionInputDelegate")
_UICollectionPreferredSizingCustomizations = _Class(
    "_UICollectionPreferredSizingCustomizations"
)
_UITextDraggableGeometrySameViewDropOperation = _Class(
    "_UITextDraggableGeometrySameViewDropOperation"
)
_UITextDragCaretUpdate = _Class("_UITextDragCaretUpdate")
_UIPositionedAttributedString = _Class("_UIPositionedAttributedString")
UITextDropRequest = _Class("UITextDropRequest")
UITextDraggableGeometrySameViewDropOperationResult = _Class(
    "UITextDraggableGeometrySameViewDropOperationResult"
)
UITextDraggableObject = _Class("UITextDraggableObject")
UITextDragRequest = _Class("UITextDragRequest")
UITextDragPreviewRenderer = _Class("UITextDragPreviewRenderer")
UITextDragFinishState = _Class("UITextDragFinishState")
UISceneSizeRestrictions = _Class("UISceneSizeRestrictions")
UIWindowSceneTouchCancellationOnRotationAssertion = _Class(
    "UIWindowSceneTouchCancellationOnRotationAssertion"
)
UISceneDestructionRequestOptions = _Class("UISceneDestructionRequestOptions")
UIWindowSceneDestructionRequestOptions = _Class(
    "UIWindowSceneDestructionRequestOptions"
)
UISubTest = _Class("UISubTest")
_UITableViewCellReuseParameters = _Class("_UITableViewCellReuseParameters")
_UITableViewShadowUpdatesController = _Class("_UITableViewShadowUpdatesController")
_UITableViewPrefetchContext = _Class("_UITableViewPrefetchContext")
UIListContentTextProperties = _Class("UIListContentTextProperties")
_UIFontPickerFontInfo = _Class("_UIFontPickerFontInfo")
_UITableViewDeleteAnimationSupport = _Class("_UITableViewDeleteAnimationSupport")
_UITableViewIndexEntry = _Class("_UITableViewIndexEntry")
_UIPointerContentEffect = _Class("_UIPointerContentEffect")
UITableViewDataSource = _Class("UITableViewDataSource")
UITableViewSection = _Class("UITableViewSection")
UITableViewRow = _Class("UITableViewRow")
_UITableViewCellPromiseRegion = _Class("_UITableViewCellPromiseRegion")
UITableViewRowAction = _Class("UITableViewRowAction")
_UIDisplayInfoProvider = _Class("_UIDisplayInfoProvider")
_UIDatePickerCalendarTimeWheelDisplayModeDriver = _Class(
    "_UIDatePickerCalendarTimeWheelDisplayModeDriver"
)
UILocalizedIndexedCollation = _Class("UILocalizedIndexedCollation")
_UITableViewSpringLoadedEffect = _Class("_UITableViewSpringLoadedEffect")
_UITableViewSpringLoadedBehavior = _Class("_UITableViewSpringLoadedBehavior")
_UITableViewSpringLoadedInteraction = _Class("_UITableViewSpringLoadedInteraction")
UITableViewPlaceholder = _Class("UITableViewPlaceholder")
UITableViewDropPlaceholder = _Class("UITableViewDropPlaceholder")
_UITableViewDropPlaceholderContextImpl = _Class(
    "_UITableViewDropPlaceholderContextImpl"
)
_UITableViewDropCoordinatorImpl = _Class("_UITableViewDropCoordinatorImpl")
_UITableViewDropItemImpl = _Class("_UITableViewDropItemImpl")
_UIKeyboardMediaServiceWarmUpConnection = _Class(
    "_UIKeyboardMediaServiceWarmUpConnection"
)
_UIClickHighlightInteractionEffect = _Class("_UIClickHighlightInteractionEffect")
_UITableViewDropAnimation = _Class("_UITableViewDropAnimation")
_UITableViewDropAnimationToTarget = _Class("_UITableViewDropAnimationToTarget")
_UITableViewDropAnimationToCell = _Class("_UITableViewDropAnimationToCell")
_UITableViewDragItemContext = _Class("_UITableViewDragItemContext")
UITableConstants_TV = _Class("UITableConstants_TV")
_UIListSeparatorConfiguration = _Class("_UIListSeparatorConfiguration")
UITableConstants_CarPlay = _Class("UITableConstants_CarPlay")
_UIPageControlVisualProvider = _Class("_UIPageControlVisualProvider")
_UIInteractivePageControlVisualProvider = _Class(
    "_UIInteractivePageControlVisualProvider"
)
_UILegacyPageControlVisualProvider = _Class("_UILegacyPageControlVisualProvider")
_UIDefaultSwipeViewManipulator = _Class("_UIDefaultSwipeViewManipulator")
UITableViewCellEditingData = _Class("UITableViewCellEditingData")
_UISwipeActionSpringAnimationParameters = _Class(
    "_UISwipeActionSpringAnimationParameters"
)
UISwipeOccurrence = _Class("UISwipeOccurrence")
UISwipeActionsConfiguration = _Class("UISwipeActionsConfiguration")
UIListContentConfiguration = _Class("UIListContentConfiguration")
_UIStoryboardUnwindChain = _Class("_UIStoryboardUnwindChain")
UIStoryboardViewControllerPlaceholder = _Class("UIStoryboardViewControllerPlaceholder")
UIStoryboardPreviewingSegueTemplateStorage = _Class(
    "UIStoryboardPreviewingSegueTemplateStorage"
)
UIStoryboardPreviewingRegistrant = _Class("UIStoryboardPreviewingRegistrant")
UIStatusBarStyleRequest = _Class("UIStatusBarStyleRequest")
UIMutableStatusBarStyleRequest = _Class("UIMutableStatusBarStyleRequest")
UIStatusBarLayoutManager = _Class("UIStatusBarLayoutManager")
UIStatusBarItem = _Class("UIStatusBarItem")
UIUserInterfaceStyleArbiterTransition = _Class("UIUserInterfaceStyleArbiterTransition")
UIUserInterfaceStyleArbiter = _Class("UIUserInterfaceStyleArbiter")
UIStatusBarComposedData = _Class("UIStatusBarComposedData")
UIStatusBarCache = _Class("UIStatusBarCache")
UIStatusBarStyleAttributes = _Class("UIStatusBarStyleAttributes")
UIStatusBarNewUIStyleAttributes = _Class("UIStatusBarNewUIStyleAttributes")
UIStatusBarNewUIActionableStyleAttributes = _Class(
    "UIStatusBarNewUIActionableStyleAttributes"
)
UIStatusBarNewUIDoubleHeightStyleAttributes = _Class(
    "UIStatusBarNewUIDoubleHeightStyleAttributes"
)
UIStatusBarLockScreenStyleAttributes = _Class("UIStatusBarLockScreenStyleAttributes")
UIStatusBarActionableLockScreenStyleAttributes = _Class(
    "UIStatusBarActionableLockScreenStyleAttributes"
)
UIStatusBarExternalStyleAttributes = _Class("UIStatusBarExternalStyleAttributes")
UIStatusBarPublisher = _Class("UIStatusBarPublisher")
UIStatusBarServer = _Class("UIStatusBarServer")
UIStatusBarServerListener = _Class("UIStatusBarServerListener")
_UIStatusBarStyleAttributes = _Class("_UIStatusBarStyleAttributes")
_UIFocusSearchInfo = _Class("_UIFocusSearchInfo")
_UIStatusBarRegion = _Class("_UIStatusBarRegion")
_UIStatusBarImageProvider = _Class("_UIStatusBarImageProvider")
_UIStatusBarDisplayItemRelation = _Class("_UIStatusBarDisplayItemRelation")
_UIStatusBarDisplayItemDependencyRelation = _Class(
    "_UIStatusBarDisplayItemDependencyRelation"
)
_UIStatusBarDisplayItemGroupRelation = _Class("_UIStatusBarDisplayItemGroupRelation")
_UIStatusBarDisplayItemState = _Class("_UIStatusBarDisplayItemState")
_UIStatusBarDisplayItemPlacementState = _Class("_UIStatusBarDisplayItemPlacementState")
_UICopyConfiguration = _Class("_UICopyConfiguration")
_UIStatusBarDataConverter = _Class("_UIStatusBarDataConverter")
_UIStatusBarDataAggregatorUpdate = _Class("_UIStatusBarDataAggregatorUpdate")
_UIStatusBarDataAggregator = _Class("_UIStatusBarDataAggregator")
_UIStatusBarData = _Class("_UIStatusBarData")
_UIStatusBarDataEntry = _Class("_UIStatusBarDataEntry")
_UIStatusBarDataBackgroundActivityEntry = _Class(
    "_UIStatusBarDataBackgroundActivityEntry"
)
_UIStatusBarDataLockEntry = _Class("_UIStatusBarDataLockEntry")
_UIStatusBarDataVoiceControlEntry = _Class("_UIStatusBarDataVoiceControlEntry")
_UIStatusBarDataLocationEntry = _Class("_UIStatusBarDataLocationEntry")
_UIStatusBarDataTetheringEntry = _Class("_UIStatusBarDataTetheringEntry")
_UIStatusBarDataActivityEntry = _Class("_UIStatusBarDataActivityEntry")
_UIStatusBarDataThermalEntry = _Class("_UIStatusBarDataThermalEntry")
_UIStatusBarDataBluetoothEntry = _Class("_UIStatusBarDataBluetoothEntry")
_UIStatusBarDataBatteryEntry = _Class("_UIStatusBarDataBatteryEntry")
_UIStatusBarDataIntegerEntry = _Class("_UIStatusBarDataIntegerEntry")
_UIStatusBarDataNetworkEntry = _Class("_UIStatusBarDataNetworkEntry")
_UIStatusBarDataWifiEntry = _Class("_UIStatusBarDataWifiEntry")
_UIStatusBarDataCellularEntry = _Class("_UIStatusBarDataCellularEntry")
_UIStatusBarDataStringEntry = _Class("_UIStatusBarDataStringEntry")
_UIStatusBarDataBoolEntry = _Class("_UIStatusBarDataBoolEntry")
_UIStatusBarCycleAnimation = _Class("_UIStatusBarCycleAnimation")
_UIStatusBarCycleLayerAnimation = _Class("_UIStatusBarCycleLayerAnimation")
_UIStatusBarAnimationFactory = _Class("_UIStatusBarAnimationFactory")
_UIStatusBarFadeAnimationParameters = _Class("_UIStatusBarFadeAnimationParameters")
_UIStatusBarAnimation = _Class("_UIStatusBarAnimation")
_UIStatusBarAction = _Class("_UIStatusBarAction")
_UIStatusBarHoverRegionAction = _Class("_UIStatusBarHoverRegionAction")
_UIStatusBarSystemNavigationAction = _Class("_UIStatusBarSystemNavigationAction")
_UIStatusBarActivityAction = _Class("_UIStatusBarActivityAction")
_UIStatusBarVisualProvider_iOS = _Class("_UIStatusBarVisualProvider_iOS")
_UIStatusBarVisualProvider_Pad = _Class("_UIStatusBarVisualProvider_Pad")
_UIStatusBarVisualProvider_Pad_ForcedNoCell = _Class(
    "_UIStatusBarVisualProvider_Pad_ForcedNoCell"
)
_UIStatusBarVisualProvider_Pad_ForcedCellular = _Class(
    "_UIStatusBarVisualProvider_Pad_ForcedCellular"
)
_UIStatusBarVisualProvider_RoundedPad = _Class("_UIStatusBarVisualProvider_RoundedPad")
_UIStatusBarVisualProvider_RoundedPad_ForcedNoCell = _Class(
    "_UIStatusBarVisualProvider_RoundedPad_ForcedNoCell"
)
_UIStatusBarVisualProvider_RoundedPad_ForcedCellular = _Class(
    "_UIStatusBarVisualProvider_RoundedPad_ForcedCellular"
)
_UIStatusBarVisualProvider_Phone = _Class("_UIStatusBarVisualProvider_Phone")
_UIStatusBarVisualProvider_Split = _Class("_UIStatusBarVisualProvider_Split")
_UIStatusBarVisualProvider_Split65 = _Class("_UIStatusBarVisualProvider_Split65")
_UIStatusBarVisualProvider_Split2x61 = _Class("_UIStatusBarVisualProvider_Split2x61")
_UIStatusBarVisualProvider_Split58 = _Class("_UIStatusBarVisualProvider_Split58")
_UIStatusBarVisualProvider_LegacyPhone = _Class(
    "_UIStatusBarVisualProvider_LegacyPhone"
)
_UIStatusBarVisualProvider_Fallback = _Class("_UIStatusBarVisualProvider_Fallback")
_UIDatePickerCalendarTimeWheelItem = _Class("_UIDatePickerCalendarTimeWheelItem")
UIKeyboardFloatingTransitionState = _Class("UIKeyboardFloatingTransitionState")
_UIBatteryViewAXHUDImageCacheInfo = _Class("_UIBatteryViewAXHUDImageCacheInfo")
_UIStatusBarRegionAxisStackingLayout = _Class("_UIStatusBarRegionAxisStackingLayout")
_UIStatusBarRegionAxisFillingLayout = _Class("_UIStatusBarRegionAxisFillingLayout")
_UIStatusBarRegionAxisCenteringLayout = _Class("_UIStatusBarRegionAxisCenteringLayout")
_UIStatusBarRegionAxisAligningLayout = _Class("_UIStatusBarRegionAxisAligningLayout")
_UIStatusBarRegionAxesLayout = _Class("_UIStatusBarRegionAxesLayout")
_UIStatusBarItemUpdate = _Class("_UIStatusBarItemUpdate")
_UIStatusBarIdentifier = _Class("_UIStatusBarIdentifier")
_UIStatusBarDisplayItemPlacement = _Class("_UIStatusBarDisplayItemPlacement")
_UIStatusBarDisplayItem = _Class("_UIStatusBarDisplayItem")
_UIStatusBarSpacerDisplayItem = _Class("_UIStatusBarSpacerDisplayItem")
_UIStatusBarDisplayItemPlacementGroup = _Class("_UIStatusBarDisplayItemPlacementGroup")
_UIStatusBarDisplayItemPlacementWifiGroup = _Class(
    "_UIStatusBarDisplayItemPlacementWifiGroup"
)
_UIStatusBarDisplayItemPlacementNetworkGroup = _Class(
    "_UIStatusBarDisplayItemPlacementNetworkGroup"
)
_UIStatusBarDisplayItemPlacementIndicatorsGroup = _Class(
    "_UIStatusBarDisplayItemPlacementIndicatorsGroup"
)
_UIStatusBarDisplayItemPlacementExpandedIndicatorsGroup = _Class(
    "_UIStatusBarDisplayItemPlacementExpandedIndicatorsGroup"
)
_UIStatusBarDisplayItemPlacementCellularGroup = _Class(
    "_UIStatusBarDisplayItemPlacementCellularGroup"
)
_UIStatusBarDisplayItemPlacementBatteryGroup = _Class(
    "_UIStatusBarDisplayItemPlacementBatteryGroup"
)
_UIPageIndicatorFeed = _Class("_UIPageIndicatorFeed")
UIStatusBarForegroundStyleAttributes = _Class("UIStatusBarForegroundStyleAttributes")
UIStatusBarLockScreenForegroundStyleAttributes = _Class(
    "UIStatusBarLockScreenForegroundStyleAttributes"
)
UIStatusBarExternalForegroundStyleAttributes = _Class(
    "UIStatusBarExternalForegroundStyleAttributes"
)
UIStatusBarExternalNavigationForegroundStyleAttributes = _Class(
    "UIStatusBarExternalNavigationForegroundStyleAttributes"
)
UIStatusBarExternalInCallForegroundStyleAttributes = _Class(
    "UIStatusBarExternalInCallForegroundStyleAttributes"
)
UIStatusBarExternalTranslucentForegroundStyleAttributes = _Class(
    "UIStatusBarExternalTranslucentForegroundStyleAttributes"
)
_UIBanner = _Class("_UIBanner")
_UIBannerContent = _Class("_UIBannerContent")
_UIStateRestorationKeyedArchiverDelegate = _Class(
    "_UIStateRestorationKeyedArchiverDelegate"
)
_UIObjectIdentifierPathProxy = _Class("_UIObjectIdentifierPathProxy")
_UIStoryboardProxy = _Class("_UIStoryboardProxy")
_UIValuePredictor = _Class("_UIValuePredictor")
_UITouchPredictor = _Class("_UITouchPredictor")
_UIDropInteractionWeakWrapper = _Class("_UIDropInteractionWeakWrapper")
_UIDragEventSample = _Class("_UIDragEventSample")
_UIStateMachine = _Class("_UIStateMachine")
_UIHIDScaleEventTracker = _Class("_UIHIDScaleEventTracker")
_UIHIDPathCollection = _Class("_UIHIDPathCollection")
_UIHIDPath = _Class("_UIHIDPath")
_UIEstimatedTouchRecord = _Class("_UIEstimatedTouchRecord")
_UIHoverTouchDeliveryTable = _Class("_UIHoverTouchDeliveryTable")
_UISlotId = _Class("_UISlotId")
_UIPopoverSceneManager = _Class("_UIPopoverSceneManager")
_UITouchDownClickInteractionDriver = _Class("_UITouchDownClickInteractionDriver")
_UISearchPresentationAssistant = _Class("_UISearchPresentationAssistant")
_UIFocusCastingController = _Class("_UIFocusCastingController")
_UIDefaultsInterfaceStyleObserver = _Class("_UIDefaultsInterfaceStyleObserver")
UIKeyCommandDiscoverabilityHUDVisualStyle = _Class(
    "UIKeyCommandDiscoverabilityHUDVisualStyle"
)
UIKeyCommandDiscoverabilityHUDVisualStyleRegular = _Class(
    "UIKeyCommandDiscoverabilityHUDVisualStyleRegular"
)
UIKeyCommandDiscoverabilityHUDVisualStyleCompact = _Class(
    "UIKeyCommandDiscoverabilityHUDVisualStyleCompact"
)
_UITouchForceMessage = _Class("_UITouchForceMessage")
_UITouchForceObservationMessageReader = _Class("_UITouchForceObservationMessageReader")
_UICollectionLayoutSectionSolver = _Class("_UICollectionLayoutSectionSolver")
_UIForceMessage = _Class("_UIForceMessage")
UIPrinterPickerControllerInternals = _Class("UIPrinterPickerControllerInternals")
_UIClickPresentationAssistant = _Class("_UIClickPresentationAssistant")
UIPrinterInternals = _Class("UIPrinterInternals")
UIPrintPreviewState = _Class("UIPrintPreviewState")
UIPrintInfoRequest = _Class("UIPrintInfoRequest")
UIPrintingProgress = _Class("UIPrintingProgress")
UIPrintPanelViewController = _Class("UIPrintPanelViewController")
_NSDiffableDataSourceSectionSnapshotState = _Class(
    "_NSDiffableDataSourceSectionSnapshotState"
)
_UIPickerViewTestParameters = _Class("_UIPickerViewTestParameters")
_UIDatePickerMode = _Class("_UIDatePickerMode")
_UIDatePickerMode_Custom = _Class("_UIDatePickerMode_Custom")
_UIDatePickerMode_TimeInterval = _Class("_UIDatePickerMode_TimeInterval")
_UIDatePickerMode_DateAndTime = _Class("_UIDatePickerMode_DateAndTime")
_UIDatePickerMode_Time = _Class("_UIDatePickerMode_Time")
_UIDatePickerMode_Date = _Class("_UIDatePickerMode_Date")
_UIDatePickerMode_YearMonth = _Class("_UIDatePickerMode_YearMonth")
_UIDatePickerMode_MonthDay = _Class("_UIDatePickerMode_MonthDay")
_UIDatePickerMode_DateWithOptionalYear = _Class(
    "_UIDatePickerMode_DateWithOptionalYear"
)
_UIDatePickerComponent = _Class("_UIDatePickerComponent")
_UICPILiveDragPreview = _Class("_UICPILiveDragPreview")
_UIDiffableDataSource = _Class("_UIDiffableDataSource")
_UIDiffableDataSourceSnapshotter = _Class("_UIDiffableDataSourceSnapshotter")
_UITableViewDiffableDataSource = _Class("_UITableViewDiffableDataSource")
_UICollectionViewDiffableDataSource = _Class("_UICollectionViewDiffableDataSource")
_UIDiffableDataSourceSnapshot = _Class("_UIDiffableDataSourceSnapshot")
_UIPreviewInteractionClassicImpl = _Class("_UIPreviewInteractionClassicImpl")
_UIPreviewInteractionViewControllerPresentation = _Class(
    "_UIPreviewInteractionViewControllerPresentation"
)
_UIPreviewInteractionHighlighter = _Class("_UIPreviewInteractionHighlighter")
UIPreviewItemController = _Class("UIPreviewItemController")
_UIPreviewInteractionPresentationTransition = _Class(
    "_UIPreviewInteractionPresentationTransition"
)
_UIPreviewInteractionDismissTransition = _Class(
    "_UIPreviewInteractionDismissTransition"
)
_UIPreviewInteractionController = _Class("_UIPreviewInteractionController")
_UIInteractionEffect_deprecated = _Class("_UIInteractionEffect_deprecated")
_UIStatusBarVisualProvider_CarPlay = _Class("_UIStatusBarVisualProvider_CarPlay")
_UIStatusBarVisualProvider_CarPlayHorizontal = _Class(
    "_UIStatusBarVisualProvider_CarPlayHorizontal"
)
_UIStatusBarVisualProvider_CarPlayVertical = _Class(
    "_UIStatusBarVisualProvider_CarPlayVertical"
)
_UIDynamicTransformer = _Class("_UIDynamicTransformer")
_UIIndexPathIdentityTracker = _Class("_UIIndexPathIdentityTracker")
_UIPreviewInteractionSystemHighlighter = _Class(
    "_UIPreviewInteractionSystemHighlighter"
)
_UIPreviewInteractionCustomViewHighlighter = _Class(
    "_UIPreviewInteractionCustomViewHighlighter"
)
_UIPreviewTransitionDelegate = _Class("_UIPreviewTransitionDelegate")
UIScribbleInteractionWrapper = _Class("UIScribbleInteractionWrapper")
_UIPreviewPresentationAnimator = _Class("_UIPreviewPresentationAnimator")
UIPreviewInteractionController = _Class("UIPreviewInteractionController")
UIInteractionProgress = _Class("UIInteractionProgress")
UIPreviewForceInteractionProgress = _Class("UIPreviewForceInteractionProgress")
_UITouchForceInteractionProgress = _Class("_UITouchForceInteractionProgress")
UIForceStageInteractionProgress = _Class("UIForceStageInteractionProgress")
UISimpleInteractionProgress = _Class("UISimpleInteractionProgress")
_UIPICSimpleInteractionProgress = _Class("_UIPICSimpleInteractionProgress")
UIForcePresentationHelper = _Class("UIForcePresentationHelper")
_UIPreviewInteractionCrossBlurViewControllerTransition = _Class(
    "_UIPreviewInteractionCrossBlurViewControllerTransition"
)
_UIPreviewInteractionViewControllerHelper = _Class(
    "_UIPreviewInteractionViewControllerHelper"
)
_UIPreviewInteractionSimulatingTouchForceProvider = _Class(
    "_UIPreviewInteractionSimulatingTouchForceProvider"
)
_UIPreviewInteractionGestureRecognizerTouchForceProvider = _Class(
    "_UIPreviewInteractionGestureRecognizerTouchForceProvider"
)
_UIPreviewInteractionDecayTouchForceProvider = _Class(
    "_UIPreviewInteractionDecayTouchForceProvider"
)
_UICommandInternalDiff = _Class("_UICommandInternalDiff")
_UICommandParentInserts = _Class("_UICommandParentInserts")
_UICommandChildInserts = _Class("_UICommandChildInserts")
_UIPreviewInteractionCompatibilityTouchForceProvider = _Class(
    "_UIPreviewInteractionCompatibilityTouchForceProvider"
)
_UIPreviewInteractionStateRecognizer = _Class("_UIPreviewInteractionStateRecognizer")
_UICollectionViewAnimator = _Class("_UICollectionViewAnimator")
_UICollectionViewAnimationContext = _Class("_UICollectionViewAnimationContext")
_UIDeepPressAnalyzer = _Class("_UIDeepPressAnalyzer")
_UIPreviewInteractionCommitTransition = _Class("_UIPreviewInteractionCommitTransition")
_UIInteractiveHighlightEffect = _Class("_UIInteractiveHighlightEffect")
_UIInteractiveHighlightEnvironment = _Class("_UIInteractiveHighlightEnvironment")
_UIInteractiveHighlightViewRecord = _Class("_UIInteractiveHighlightViewRecord")
_UIElasticValue = _Class("_UIElasticValue")
NSDiffableDataSourceSectionTransaction = _Class(
    "NSDiffableDataSourceSectionTransaction"
)
NSDiffableDataSourceTransaction = _Class("NSDiffableDataSourceTransaction")
_UIVelocityIntegrator = _Class("_UIVelocityIntegrator")
_UIVelocityIntegratorDataSample = _Class("_UIVelocityIntegratorDataSample")
_UIPreviewActionsController = _Class("_UIPreviewActionsController")
_UIPlatterMenuPanningTransformer = _Class("_UIPlatterMenuPanningTransformer")
_UIPlatterMenuDynamicsController = _Class("_UIPlatterMenuDynamicsController")
_UIPlatterItem = _Class("_UIPlatterItem")
_UIViewControllerPreviewingContext = _Class("_UIViewControllerPreviewingContext")
_UIViewControllerCompatibilityPreviewingContext = _Class(
    "_UIViewControllerCompatibilityPreviewingContext"
)
UIKBPhoneToCarPlayTransformation = _Class("UIKBPhoneToCarPlayTransformation")
_UIInertPreviewingContext = _Class("_UIInertPreviewingContext")
_UIItemProviderRepresentationOptions = _Class("_UIItemProviderRepresentationOptions")
_UIContentViewEditingState = _Class("_UIContentViewEditingState")
_UIContentViewEditingConfiguration = _Class("_UIContentViewEditingConfiguration")
UIFocusRingClientState = _Class("UIFocusRingClientState")
UIUserNotificationAction = _Class("UIUserNotificationAction")
UIMutableUserNotificationAction = _Class("UIMutableUserNotificationAction")
UIUserNotificationCategory = _Class("UIUserNotificationCategory")
UIMutableUserNotificationCategory = _Class("UIMutableUserNotificationCategory")
UIUserNotificationSettings = _Class("UIUserNotificationSettings")
UIUserNotificationActionSettings = _Class("UIUserNotificationActionSettings")
UIMutableUserNotificationActionSettings = _Class(
    "UIMutableUserNotificationActionSettings"
)
_UIKeyboardPasscodeObscuringInteraction = _Class(
    "_UIKeyboardPasscodeObscuringInteraction"
)
_UISheetDropInteraction = _Class("_UISheetDropInteraction")
UILocalNotification = _Class("UILocalNotification")
UIConcreteLocalNotification = _Class("UIConcreteLocalNotification")
_UIMotionEffectAcceleratedOutputRange = _Class("_UIMotionEffectAcceleratedOutputRange")
UIMotionEffect = _Class("UIMotionEffect")
_UITiltMotionEffect = _Class("_UITiltMotionEffect")
_UIParallaxMotionEffect = _Class("_UIParallaxMotionEffect")
UIMotionEffectGroup = _Class("UIMotionEffectGroup")
UIInterpolatingMotionEffect = _Class("UIInterpolatingMotionEffect")
_UIViewerRelativeDevicePose = _Class("_UIViewerRelativeDevicePose")
_UIMotionEffectEngineLogger = _Class("_UIMotionEffectEngineLogger")
_UIMotionEffectEngineClient = _Class("_UIMotionEffectEngineClient")
_UIMotionEffectEventProvider = _Class("_UIMotionEffectEventProvider")
_UIMotionEffectCoreMotionEventProvider = _Class(
    "_UIMotionEffectCoreMotionEventProvider"
)
_UIMotionEffectEvent = _Class("_UIMotionEffectEvent")
_UIMotionEffectFocusChangeEvent = _Class("_UIMotionEffectFocusChangeEvent")
_UIMotionEffectAttitudeEvent = _Class("_UIMotionEffectAttitudeEvent")
_UIMotionEffectApplicator = _Class("_UIMotionEffectApplicator")
_UICAAnimationPositionQuantizer = _Class("_UICAAnimationPositionQuantizer")
_UIMotionAnalyzer = _Class("_UIMotionAnalyzer")
_UIMotionFocusAnalyzer = _Class("_UIMotionFocusAnalyzer")
_UIMotionAttitudeAnalyzer = _Class("_UIMotionAttitudeAnalyzer")
_UIValueCellContentViewConfiguration = _Class("_UIValueCellContentViewConfiguration")
_UIInputHostController = _Class("_UIInputHostController")
UIKBUndoStyling = _Class("UIKBUndoStyling")
_PointQueue = _Class("_PointQueue")
_PathPoint = _Class("_PathPoint")
UITextInputPayloadController = _Class("UITextInputPayloadController")
UITextSuggestion = _Class("UITextSuggestion")
UIAutofillExtrasSuggestion = _Class("UIAutofillExtrasSuggestion")
UITextAutofillSuggestion = _Class("UITextAutofillSuggestion")
_UISubtitleCellContentViewConfiguration = _Class(
    "_UISubtitleCellContentViewConfiguration"
)
UIKeyboardKeyplaneTransition = _Class("UIKeyboardKeyplaneTransition")
UIKeyboardSquishTransition = _Class("UIKeyboardSquishTransition")
UIKeyboardShiftTransition = _Class("UIKeyboardShiftTransition")
UIKeyboardKeySwipeTransition = _Class("UIKeyboardKeySwipeTransition")
UIKeyboardHandBiasTransitionContext = _Class("UIKeyboardHandBiasTransitionContext")
UIKBPanGestureVelocitySample = _Class("UIKBPanGestureVelocitySample")
_UIPointerContentEffectAnimationBuilder = _Class(
    "_UIPointerContentEffectAnimationBuilder"
)
_UIPageIndicatorStore = _Class("_UIPageIndicatorStore")
_UIPageIndicatorStoreObject = _Class("_UIPageIndicatorStoreObject")
_UIFocusGroupHistory = _Class("_UIFocusGroupHistory")
_UIKBRTFingerInfo = _Class("_UIKBRTFingerInfo")
_UIKBRTFakeFingerInfo = _Class("_UIKBRTFakeFingerInfo")
_UIKBRTMutableOrderIndexSet = _Class("_UIKBRTMutableOrderIndexSet")
_UIKBRTTouchVelocities = _Class("_UIKBRTTouchVelocities")
_UIKBRTTimerBlock = _Class("_UIKBRTTimerBlock")
_UIKBRTTouchHistory = _Class("_UIKBRTTouchHistory")
_UIKBRTTouchHistoryInfo = _Class("_UIKBRTTouchHistoryInfo")
_UIKBRTDecayingObject = _Class("_UIKBRTDecayingObject")
_UIKBRTDecayingOffset = _Class("_UIKBRTDecayingOffset")
_UIFocusGroup = _Class("_UIFocusGroup")
_UIKBRTRecognizer = _Class("_UIKBRTRecognizer")
_UIKBRTConfidenceLevels = _Class("_UIKBRTConfidenceLevels")
_UIKBRTPendingConfidenceLevels = _Class("_UIKBRTPendingConfidenceLevels")
_UIKBRTObject = _Class("_UIKBRTObject")
_UIKBRTTouchInfo = _Class("_UIKBRTTouchInfo")
_UIKBRTKeyboardTouchObserver = _Class("_UIKBRTKeyboardTouchObserver")
_UIKBRTFingerDetection = _Class("_UIKBRTFingerDetection")
_UIKBRTTouchDrifting = _Class("_UIKBRTTouchDrifting")
UIKBCadenceMonitor = _Class("UIKBCadenceMonitor")
UIKeyboardSupplementaryControlKeyTransformation = _Class(
    "UIKeyboardSupplementaryControlKeyTransformation"
)
UIKBKeyplaneTransformationContext = _Class("UIKBKeyplaneTransformationContext")
UIKBContinuousPathModalKeysTransformation = _Class(
    "UIKBContinuousPathModalKeysTransformation"
)
_UIKBVoidSpace = _Class("_UIKBVoidSpace")
UIPointerShape = _Class("UIPointerShape")
_UICursor = _Class("_UICursor")
UIPointerStyle = _Class("UIPointerStyle")
_UICursorStyle = _Class("_UICursorStyle")
UIPointerEffect = _Class("UIPointerEffect")
_UICursorEffect = _Class("_UICursorEffect")
_UICursorHoverEffect = _Class("_UICursorHoverEffect")
_UICursorLiftEffect = _Class("_UICursorLiftEffect")
_UICursorAppIconEffect = _Class("_UICursorAppIconEffect")
_UICursorHighlightEffect = _Class("_UICursorHighlightEffect")
_UIPointerScrollIndicatorEffect = _Class("_UIPointerScrollIndicatorEffect")
UIPointerHoverEffect = _Class("UIPointerHoverEffect")
_UIPointerAccessibilityEffect = _Class("_UIPointerAccessibilityEffect")
UIPointerLiftEffect = _Class("UIPointerLiftEffect")
UIPointerAppIconEffect = _Class("UIPointerAppIconEffect")
UIPointerHighlightEffect = _Class("UIPointerHighlightEffect")
_UISwipeAnimationFactory = _Class("_UISwipeAnimationFactory")
UIKeyboardPopoverContainer = _Class("UIKeyboardPopoverContainer")
UICellAccessory = _Class("UICellAccessory")
UICellAccessoryCustomView = _Class("UICellAccessoryCustomView")
UICellAccessoryLabel = _Class("UICellAccessoryLabel")
UICellAccessoryOutlineDisclosure = _Class("UICellAccessoryOutlineDisclosure")
UICellAccessoryMultiselect = _Class("UICellAccessoryMultiselect")
UICellAccessorySeparator = _Class("UICellAccessorySeparator")
UICellAccessoryReorder = _Class("UICellAccessoryReorder")
UICellAccessoryInsert = _Class("UICellAccessoryInsert")
UICellAccessoryDelete = _Class("UICellAccessoryDelete")
UICellAccessoryCheckmark = _Class("UICellAccessoryCheckmark")
UICellAccessoryDisclosureIndicator = _Class("UICellAccessoryDisclosureIndicator")
_UICollectionViewLayoutSwipeViewManipulator = _Class(
    "_UICollectionViewLayoutSwipeViewManipulator"
)
_UICollectionViewLayoutSwipeActionsModule = _Class(
    "_UICollectionViewLayoutSwipeActionsModule"
)
UIInputViewAnimationStyleExtraView = _Class("UIInputViewAnimationStyleExtraView")
UIKeyboardRotationState = _Class("UIKeyboardRotationState")
UIInputViewTransition = _Class("UIInputViewTransition")
UIPeripheralHostState = _Class("UIPeripheralHostState")
UIKBDerivedKeyboard = _Class("UIKBDerivedKeyboard")
UIKBSplitTraits = _Class("UIKBSplitTraits")
UIKBTouchOrderedTaskList = _Class("UIKBTouchOrderedTaskList")
UIKBTouchStateTask = _Class("UIKBTouchStateTask")
UIKBTouchState = _Class("UIKBTouchState")
UIKeyboardInputManagerMux = _Class("UIKeyboardInputManagerMux")
UIKeyboardInputManagerClient = _Class("UIKeyboardInputManagerClient")
UIKeyboardInputManagerClientRequest = _Class("UIKeyboardInputManagerClientRequest")
UIKeyboardDockItem = _Class("UIKeyboardDockItem")
_UIKeyboardAnimatorAnimationStyleControllerContext = _Class(
    "_UIKeyboardAnimatorAnimationStyleControllerContext"
)
_UIKeyboardAnimatorAnimationStyleController = _Class(
    "_UIKeyboardAnimatorAnimationStyleController"
)
_UIKeyboardAnimator = _Class("_UIKeyboardAnimator")
_UICGColorCacheKey = _Class("_UICGColorCacheKey")
UIKBViewTreeSnapshotter = _Class("UIKBViewTreeSnapshotter")
UIKeyboardEmojiPreferences = _Class("UIKeyboardEmojiPreferences")
UIKeyboardEmojiKeyDisplayController = _Class("UIKeyboardEmojiKeyDisplayController")
UIKeyboardEmojiGraphicsTraits = _Class("UIKeyboardEmojiGraphicsTraits")
UIKeyboardEmojiGraphics = _Class("UIKeyboardEmojiGraphics")
UIKeyboardEmojiCategory = _Class("UIKeyboardEmojiCategory")
UIKeyboardEmoji = _Class("UIKeyboardEmoji")
_IntArray2D = _Class("_IntArray2D")
_EditScriptRangedAtom = _Class("_EditScriptRangedAtom")
_EditScriptIndexedAtom = _Class("_EditScriptIndexedAtom")
_EditScriptDataArray = _Class("_EditScriptDataArray")
_EditScript = _Class("_EditScript")
_EditScriptRanged = _Class("_EditScriptRanged")
_EditScriptIndexed = _Class("_EditScriptIndexed")
UIDictationSerializableResults = _Class("UIDictationSerializableResults")
UIDictationMultilingualResults = _Class("UIDictationMultilingualResults")
UIDictationMultilingualString = _Class("UIDictationMultilingualString")
UIDictationInterpretationGroup = _Class("UIDictationInterpretationGroup")
UIDictationInterpretation = _Class("UIDictationInterpretation")
UIDictationToken = _Class("UIDictationToken")
UIDictationScoredToken = _Class("UIDictationScoredToken")
UIDictationUtilities = _Class("UIDictationUtilities")
UIDictationLandingViewSettings = _Class("UIDictationLandingViewSettings")
UIDictationConnectionFilterState = _Class("UIDictationConnectionFilterState")
DispatchGroupWrapper = _Class("DispatchGroupWrapper")
UIDictationStreamingOperations = _Class("UIDictationStreamingOperations")
UIDictationConnectionCorrectionInfo = _Class("UIDictationConnectionCorrectionInfo")
UIDictationConnectionOptions = _Class("UIDictationConnectionOptions")
UIKBStrokeSample = _Class("UIKBStrokeSample")
UIKeyboardSyntheticTouch = _Class("UIKeyboardSyntheticTouch")
UIKeyboardTouchInfo = _Class("UIKeyboardTouchInfo")
UIKBRenderer = _Class("UIKBRenderer")
UIKBDivotedEffect = _Class("UIKBDivotedEffect")
UIKBShadowEffect = _Class("UIKBShadowEffect")
UIKBNullEffect = _Class("UIKBNullEffect")
UIKBHandwritingInputSpeedModel = _Class("UIKBHandwritingInputSpeedModel")
_UIKBHandwritingInputSpeedModelPoint = _Class("_UIKBHandwritingInputSpeedModelPoint")
UIKBHandwritingPointFIFO = _Class("UIKBHandwritingPointFIFO")
UIKBHandwritingBezierPathPointFIFO = _Class("UIKBHandwritingBezierPathPointFIFO")
UIKBHandwritingQuadCurvePointFIFO = _Class("UIKBHandwritingQuadCurvePointFIFO")
UIKBHandwritingBoxcarFilterPointFIFO = _Class("UIKBHandwritingBoxcarFilterPointFIFO")
UIKBHandwritingStrokePointFIFO = _Class("UIKBHandwritingStrokePointFIFO")
UIGestureKeyboardIntroduction = _Class("UIGestureKeyboardIntroduction")
UIKBShapeOperator = _Class("UIKBShapeOperator")
_UISceneFocusMovementBSActionsHandler = _Class("_UISceneFocusMovementBSActionsHandler")
_UIInputViewControllerOutput = _Class("_UIInputViewControllerOutput")
_UIInputViewControllerState = _Class("_UIInputViewControllerState")
_UIDialogForAddingKeyboard = _Class("_UIDialogForAddingKeyboard")
UIMultiSelectInteractionState = _Class("UIMultiSelectInteractionState")
UIKeyboardSplitControlMenu_DockAndMerge = _Class(
    "UIKeyboardSplitControlMenu_DockAndMerge"
)
UIKeyboardSplitControlMenu_Merge = _Class("UIKeyboardSplitControlMenu_Merge")
UIKeyboardSplitControlMenu_Split = _Class("UIKeyboardSplitControlMenu_Split")
UIKeyboardSplitControlMenu_Dock = _Class("UIKeyboardSplitControlMenu_Dock")
UIKeyboardSplitControlMenu_Undock = _Class("UIKeyboardSplitControlMenu_Undock")
UIKeyboardSplitControlMenu_Floating = _Class("UIKeyboardSplitControlMenu_Floating")
UIInputSwitcherGestureState = _Class("UIInputSwitcherGestureState")
UIInputSwitcherItem = _Class("UIInputSwitcherItem")
UIKeyboardCandidateViewStyle = _Class("UIKeyboardCandidateViewStyle")
UIKeyboardCandidateViewState = _Class("UIKeyboardCandidateViewState")
_UIFocusLinearMovementDebugViewLineElement = _Class(
    "_UIFocusLinearMovementDebugViewLineElement"
)
_UIFocusLinearMovementDebugViewLineSegment = _Class(
    "_UIFocusLinearMovementDebugViewLineSegment"
)
UIKeyboardCandidateViewImageRenderer = _Class("UIKeyboardCandidateViewImageRenderer")
_UIDiffableSectionBoundaryMoveDetector = _Class(
    "_UIDiffableSectionBoundaryMoveDetector"
)
UIKBAutoFillTestTagRequest = _Class("UIKBAutoFillTestTagRequest")
UIKBAutoFillTestTableViewHeaderFooterData = _Class(
    "UIKBAutoFillTestTableViewHeaderFooterData"
)
UIKBTestAutoFillTableViewCellData = _Class("UIKBTestAutoFillTableViewCellData")
UIKBAutoFillTestTableViewDataSource = _Class("UIKBAutoFillTestTableViewDataSource")
UIKBAutoFillTestArchiveMaker = _Class("UIKBAutoFillTestArchiveMaker")
UIKBAutoFillTestArchive = _Class("UIKBAutoFillTestArchive")
UIKBAutoFillTestExpectedResult = _Class("UIKBAutoFillTestExpectedResult")
_UIRelationshipTraitStorageRecord = _Class("_UIRelationshipTraitStorageRecord")
_UIAttributeTraitStorageRecord = _Class("_UIAttributeTraitStorageRecord")
_UITraitStorage = _Class("_UITraitStorage")
_UIRelationshipTraitStorage = _Class("_UIRelationshipTraitStorage")
_UIColorAttributeTraitStorage = _Class("_UIColorAttributeTraitStorage")
_UIAttributeTraitStorage = _Class("_UIAttributeTraitStorage")
_UITraitStorageList = _Class("_UITraitStorageList")
_UICoreUICatalogColorWrapper = _Class("_UICoreUICatalogColorWrapper")
_UIKeyboardSuppressionPencilPolicyDelegate = _Class(
    "_UIKeyboardSuppressionPencilPolicyDelegate"
)
UIRuntimeAccessibilityConfiguration = _Class("UIRuntimeAccessibilityConfiguration")
UINibKeyValuePair = _Class("UINibKeyValuePair")
_UIClickInteraction = _Class("_UIClickInteraction")
_UIPercentDrivenInteractionEffect = _Class("_UIPercentDrivenInteractionEffect")
_UIPercentDrivenInteractionEffectChangeContext = _Class(
    "_UIPercentDrivenInteractionEffectChangeContext"
)
_UIIdleModeLayoutAttributes = _Class("_UIIdleModeLayoutAttributes")
_UIIdleModeController = _Class("_UIIdleModeController")
_UIContentViewEditingController = _Class("_UIContentViewEditingController")
_UITableViewMultiSelectController = _Class("_UITableViewMultiSelectController")
UIAccelerometer = _Class("UIAccelerometer")
UIAcceleration = _Class("UIAcceleration")
_UICachedBoundingPathBitmapDataReferenceCorner = _Class(
    "_UICachedBoundingPathBitmapDataReferenceCorner"
)
_UIBoundingPathBitmap = _Class("_UIBoundingPathBitmap")
_UILegibilityImageSet = _Class("_UILegibilityImageSet")
_UILegibilityCachedShadow = _Class("_UILegibilityCachedShadow")
_UILegibilitySettings = _Class("_UILegibilitySettings")
_UILegibilitySettingsProvider = _Class("_UILegibilitySettingsProvider")
UITextRenderingAttributes = _Class("UITextRenderingAttributes")
_UIImageAssetRenditionCacheKey = _Class("_UIImageAssetRenditionCacheKey")
_UIImageSymbolLayer = _Class("_UIImageSymbolLayer")
_UIImageSerializationWrapper = _Class("_UIImageSerializationWrapper")
_UIGraphicsLetterpressStyle = _Class("_UIGraphicsLetterpressStyle")
UIGradient = _Class("UIGradient")
_UITVScrollViewManager = _Class("_UITVScrollViewManager")
_UIForceLevelClassifier = _Class("_UIForceLevelClassifier")
_UIPreviewInteractionForceLevelClassifier = _Class(
    "_UIPreviewInteractionForceLevelClassifier"
)
_UILinearForceLevelClassifier = _Class("_UILinearForceLevelClassifier")
UICollectionViewSupplementaryRegistration = _Class(
    "UICollectionViewSupplementaryRegistration"
)
_UICollectionViewSupplementaryRegistration = _Class(
    "_UICollectionViewSupplementaryRegistration"
)
UICollectionViewCellRegistration = _Class("UICollectionViewCellRegistration")
_UICollectionViewCellRegistration = _Class("_UICollectionViewCellRegistration")
_UIContextMenuLayoutArbiter = _Class("_UIContextMenuLayoutArbiter")
_UIContextMenuLayoutArbiterOutput = _Class("_UIContextMenuLayoutArbiterOutput")
_UIContextMenuLayoutArbiterInput = _Class("_UIContextMenuLayoutArbiterInput")
UIGestureDelayedPress = _Class("UIGestureDelayedPress")
_UIDigitizerGestureRecognizerImp = _Class("_UIDigitizerGestureRecognizerImp")
__UISystemGestureManager = _Class("__UISystemGestureManager")
_UISystemGestureManager = _Class("_UISystemGestureManager")
_UIDatePickerCalendarViewDataSourceController = _Class(
    "_UIDatePickerCalendarViewDataSourceController"
)
UIInputViewAnimationControllerSlideContext = _Class(
    "UIInputViewAnimationControllerSlideContext"
)
UIInputViewAnimationControllerSlide = _Class("UIInputViewAnimationControllerSlide")
_UIArrayController = _Class("_UIArrayController")
UIKBTutorialModalDisplayStyling = _Class("UIKBTutorialModalDisplayStyling")
_UIDisplayObserver = _Class("_UIDisplayObserver")
UISnapshottingAssertionManager = _Class("UISnapshottingAssertionManager")
UISnapshottingAssertion = _Class("UISnapshottingAssertion")
UIScenePresentationManager = _Class("UIScenePresentationManager")
UIScenePresentationContext = _Class("UIScenePresentationContext")
UIMutableScenePresentationContext = _Class("UIMutableScenePresentationContext")
UISceneLayerTargetFactory = _Class("UISceneLayerTargetFactory")
UISceneLayerPresentationContext = _Class("UISceneLayerPresentationContext")
UIMutableSceneLayerPresentationContext = _Class(
    "UIMutableSceneLayerPresentationContext"
)
UIExternalScenePairingObserver = _Class("UIExternalScenePairingObserver")
_UITransformToReasonAssociation = _Class("_UITransformToReasonAssociation")
UITransform = _Class("UITransform")
UITransformer = _Class("UITransformer")
UIMutableTransformer = _Class("UIMutableTransformer")
_UIDatePickerCalendarTimeFormat = _Class("_UIDatePickerCalendarTimeFormat")
UIScenePresentationBinder = _Class("UIScenePresentationBinder")
UIRootWindowScenePresentationBinder = _Class("UIRootWindowScenePresentationBinder")
_UIScenePresenterOwner = _Class("_UIScenePresenterOwner")
_UIScenePresenter = _Class("_UIScenePresenter")
_UISceneLayerTargetWithContext = _Class("_UISceneLayerTargetWithContext")
UIApplicationSceneDeactivationManager = _Class("UIApplicationSceneDeactivationManager")
UIApplicationSceneDeactivationAssertion = _Class(
    "UIApplicationSceneDeactivationAssertion"
)
_UIPreviewInteractionClickImpl = _Class("_UIPreviewInteractionClickImpl")
UISystemNavigationActionDestinationContext = _Class(
    "UISystemNavigationActionDestinationContext"
)
UIKBResizingKeyplaneTransformation = _Class("UIKBResizingKeyplaneTransformation")
UIWebFormDelegate = _Class("UIWebFormDelegate")
_UIWebFormDelegateEditedFormsMap = _Class("_UIWebFormDelegateEditedFormsMap")
UIWebFormSelectPeripheral = _Class("UIWebFormSelectPeripheral")
UIWebOptGroup = _Class("UIWebOptGroup")
UIDOMHTMLOptGroupSelectedItem = _Class("UIDOMHTMLOptGroupSelectedItem")
UIDOMHTMLOptionSelectedItem = _Class("UIDOMHTMLOptionSelectedItem")
UIWebFormDateTimePeripheral = _Class("UIWebFormDateTimePeripheral")
UIWebRotatingNodePopover = _Class("UIWebRotatingNodePopover")
UIWebFormRotatingAccessoryPopover = _Class("UIWebFormRotatingAccessoryPopover")
UIWebSelectPopover = _Class("UIWebSelectPopover")
UIWebDefaultDateTimePopover = _Class("UIWebDefaultDateTimePopover")
UIWebDefaultDateTimePicker = _Class("UIWebDefaultDateTimePicker")
_UIWebFileUploadItem = _Class("_UIWebFileUploadItem")
_UIWebImageUploadItem = _Class("_UIWebImageUploadItem")
_UIWebVideoUploadItem = _Class("_UIWebVideoUploadItem")
_UIFocusScrollManager = _Class("_UIFocusScrollManager")
_UIFocusDisplayLinkScrollAnimator = _Class("_UIFocusDisplayLinkScrollAnimator")
_UIFocusEngineScrollableContainerOffsets = _Class(
    "_UIFocusEngineScrollableContainerOffsets"
)
_UIFocusFastScrollingRequest = _Class("_UIFocusFastScrollingRequest")
_CarTitleAlternative = _Class("_CarTitleAlternative")
_UIFocusFastScrollingRecognizer = _Class("_UIFocusFastScrollingRecognizer")
_UIFocusFastScrollingSwipeSequence = _Class("_UIFocusFastScrollingSwipeSequence")
_UIFocusFastScrollingTouchSequence = _Class("_UIFocusFastScrollingTouchSequence")
_UIFocusFastScrollingIndexBarEntryTrimmer = _Class(
    "_UIFocusFastScrollingIndexBarEntryTrimmer"
)
_UIContextMenuPresentationAnimation = _Class("_UIContextMenuPresentationAnimation")
_UICompactContextMenuPresentationAnimation = _Class(
    "_UICompactContextMenuPresentationAnimation"
)
_UIFocusFastScrollingIndexBarEntry = _Class("_UIFocusFastScrollingIndexBarEntry")
_UIFocusFastScrollingDataAggregator = _Class("_UIFocusFastScrollingDataAggregator")
_UIFocusFastScrollingEntryTrimmerDelegate = _Class(
    "_UIFocusFastScrollingEntryTrimmerDelegate"
)
_UIFocusFastScrollingController = _Class("_UIFocusFastScrollingController")
_UITextItemActionSheet = _Class("_UITextItemActionSheet")
_UIScreenFocusSystemManager = _Class("_UIScreenFocusSystemManager")
_UIFocusMovementRequest = _Class("_UIFocusMovementRequest")
_UIDefaultFocusSoundPlayer = _Class("_UIDefaultFocusSoundPlayer")
_UIFocusSoundPool = _Class("_UIFocusSoundPool")
_UIFocusSoundGenerator = _Class("_UIFocusSoundGenerator")
_UIFocusMovementPerformer = _Class("_UIFocusMovementPerformer")
_UIDefaultFocusHapticFeedbackGenerator = _Class(
    "_UIDefaultFocusHapticFeedbackGenerator"
)
UICollectionViewDiffableDataSourceSectionSnapshotHandlers = _Class(
    "UICollectionViewDiffableDataSourceSectionSnapshotHandlers"
)
_UIFocusItemFrameReporter = _Class("_UIFocusItemFrameReporter")
_UIDiffableDataSourceSectionControllerHandlers = _Class(
    "_UIDiffableDataSourceSectionControllerHandlers"
)
_UIDiffableDataSourceSectionControllerHandlersInternal = _Class(
    "_UIDiffableDataSourceSectionControllerHandlersInternal"
)
_UIDiffableDataSourceOutlineSectionControllerHandlersInternal = _Class(
    "_UIDiffableDataSourceOutlineSectionControllerHandlersInternal"
)
_UIDiffableDataSourceOutlineSectionControllerHandlers = _Class(
    "_UIDiffableDataSourceOutlineSectionControllerHandlers"
)
_UIDiffableDataSourceSectionController = _Class(
    "_UIDiffableDataSourceSectionController"
)
_UIDiffableDataSourceSectionControllerInternal = _Class(
    "_UIDiffableDataSourceSectionControllerInternal"
)
_UIDiffableDataSourceOutlineSectionControllerInternal = _Class(
    "_UIDiffableDataSourceOutlineSectionControllerInternal"
)
_UIDiffableDataSourceOutlineSectionController = _Class(
    "_UIDiffableDataSourceOutlineSectionController"
)
_UIFocusMapSnapshotter = _Class("_UIFocusMapSnapshotter")
_UIFocusMapSnapshot = _Class("_UIFocusMapSnapshot")
NSDiffableDataSourceSectionSnapshot = _Class("NSDiffableDataSourceSectionSnapshot")
_NSDiffableDataSourceSectionSnapshot = _Class("_NSDiffableDataSourceSectionSnapshot")
_NSDiffableDataSourceSectionSnapshotInternal = _Class(
    "_NSDiffableDataSourceSectionSnapshotInternal"
)
_UIFocusMapRect = _Class("_UIFocusMapRect")
_UIFocusMapSearchInfo = _Class("_UIFocusMapSearchInfo")
_UIFocusMap = _Class("_UIFocusMap")
_UIFocusRegionMapEntry = _Class("_UIFocusRegionMapEntry")
_UIFocusContainerGuideMapEntry = _Class("_UIFocusContainerGuideMapEntry")
_UIFocusableRegionMapEntry = _Class("_UIFocusableRegionMapEntry")
_UIFocusRegionMapSnapshot = _Class("_UIFocusRegionMapSnapshot")
_UIFocusRegionMapSnapshotRequest = _Class("_UIFocusRegionMapSnapshotRequest")
_UIFocusRegionMap = _Class("_UIFocusRegionMap")
_UIFocusRegionContainerProxy = _Class("_UIFocusRegionContainerProxy")
_UIFocusRegionContentAttributes = _Class("_UIFocusRegionContentAttributes")
_UIFocusRegion = _Class("_UIFocusRegion")
_UIFocusSpeedBumpRegion = _Class("_UIFocusSpeedBumpRegion")
_UIFocusPromiseRegion = _Class("_UIFocusPromiseRegion")
_UIFocusItemRegion = _Class("_UIFocusItemRegion")
_UIFocusGuideRegion = _Class("_UIFocusGuideRegion")
_UIFocusContainerGuideRegion = _Class("_UIFocusContainerGuideRegion")
_UIFocusEffectsController = _Class("_UIFocusEffectsController")
_UIFocusEngineDelayedPressAction = _Class("_UIFocusEngineDelayedPressAction")
_UIFocusEventRecognizer = _Class("_UIFocusEventRecognizer")
_UIDatePickerLinkedLabelCacheKey = _Class("_UIDatePickerLinkedLabelCacheKey")
_UIDatePickerLinkedLabelStorage = _Class("_UIDatePickerLinkedLabelStorage")
_UIFocusUpdateReport = _Class("_UIFocusUpdateReport")
_UIContextMenuInteraction = _Class("_UIContextMenuInteraction")
_UIFocusMapSnapshotDebugInfo = _Class("_UIFocusMapSnapshotDebugInfo")
_UIDebugReportComponents = _Class("_UIDebugReportComponents")
_UIDebugLogReport = _Class("_UIDebugLogReport")
_UIDebugLogStatement = _Class("_UIDebugLogStatement")
_UIDebugReportFormatter = _Class("_UIDebugReportFormatter")
_UIFocusUpdateReportFormatter = _Class("_UIFocusUpdateReportFormatter")
_UIDebugLogReportFormatter = _Class("_UIDebugLogReportFormatter")
_UIDebugIssueReportFormatter = _Class("_UIDebugIssueReportFormatter")
_UIDebugIssueReport = _Class("_UIDebugIssueReport")
_UIDebugIssue = _Class("_UIDebugIssue")
_UIFocusDebuggerStringOutput = _Class("_UIFocusDebuggerStringOutput")
_UINSLayoutManagerBaselineCalculator = _Class("_UINSLayoutManagerBaselineCalculator")
_UIFocusMovementInfo = _Class("_UIFocusMovementInfo")
_UIFocusLinearMovementSequence = _Class("_UIFocusLinearMovementSequence")
_UIFocusItemInfo = _Class("_UIFocusItemInfo")
_UIFocusInputDeviceInfo = _Class("_UIFocusInputDeviceInfo")
_UIDeepestPreferredEnvironmentSearch = _Class("_UIDeepestPreferredEnvironmentSearch")
_UIFocusEnvironmentPreferenceEnumerator = _Class(
    "_UIFocusEnvironmentPreferenceEnumerator"
)
_UIFocusEnvironmentPreferenceEnumerationContext = _Class(
    "_UIFocusEnvironmentPreferenceEnumerationContext"
)
_UITargetContentIdentifierPredicateValidator = _Class(
    "_UITargetContentIdentifierPredicateValidator"
)
_UIDatePickerCalendarTimeSoundDriver = _Class("_UIDatePickerCalendarTimeSoundDriver")
_UIFocusEngineFakePanGestureRecognizer = _Class(
    "_UIFocusEngineFakePanGestureRecognizer"
)
_UIFocusTest = _Class("_UIFocusTest")
_UIFocusSwipeTest = _Class("_UIFocusSwipeTest")
_UIFocusMoveTest = _Class("_UIFocusMoveTest")
_UIFocusFastScrollingTest = _Class("_UIFocusFastScrollingTest")
_UIFocusAnimationCoordinatorManager = _Class("_UIFocusAnimationCoordinatorManager")
_UIFocusAnimationConfiguration = _Class("_UIFocusAnimationConfiguration")
_UIFocusAnimationContext = _Class("_UIFocusAnimationContext")
_UIFeedbackVisualizer = _Class("_UIFeedbackVisualizer")
_UIFeedbackCoreHapticsPlayer = _Class("_UIFeedbackCoreHapticsPlayer")
_UIFeedbackData = _Class("_UIFeedbackData")
_UIStatusBarItem = _Class("_UIStatusBarItem")
_UIStatusBarSensorActivityItem = _Class("_UIStatusBarSensorActivityItem")
_UIStatusBarVPNDisconnectItem = _Class("_UIStatusBarVPNDisconnectItem")
_UIStatusBarFallbackItem = _Class("_UIStatusBarFallbackItem")
_UIStatusBarSpacerItem = _Class("_UIStatusBarSpacerItem")
_UIStatusBarWifiItem = _Class("_UIStatusBarWifiItem")
_UIStatusBarTimeItem = _Class("_UIStatusBarTimeItem")
_UIStatusBarNameItem = _Class("_UIStatusBarNameItem")
_UIStatusBarDeviceNameItem = _Class("_UIStatusBarDeviceNameItem")
_UIStatusBarPersonNameItem = _Class("_UIStatusBarPersonNameItem")
_UIStatusBarNavigationItem = _Class("_UIStatusBarNavigationItem")
_UIStatusBarLockItem = _Class("_UIStatusBarLockItem")
_UIStatusBarCellularItem = _Class("_UIStatusBarCellularItem")
_UIStatusBarCellularExpandedItem = _Class("_UIStatusBarCellularExpandedItem")
_UIStatusBarSecondaryCellularExpandedItem = _Class(
    "_UIStatusBarSecondaryCellularExpandedItem"
)
_UIStatusBarCellularCondensedItem = _Class("_UIStatusBarCellularCondensedItem")
_UIStatusBarSecondaryCellularCondensedItem = _Class(
    "_UIStatusBarSecondaryCellularCondensedItem"
)
_UIStatusBarBuildVersionItem = _Class("_UIStatusBarBuildVersionItem")
_UIStatusBarBatteryItem = _Class("_UIStatusBarBatteryItem")
_UIStatusBarActivityItem = _Class("_UIStatusBarActivityItem")
_UIStatusBarActivityItem_SyncOnly = _Class("_UIStatusBarActivityItem_SyncOnly")
_UIStatusBarActivityItem_Split = _Class("_UIStatusBarActivityItem_Split")
_UIStatusBarIndicatorItem = _Class("_UIStatusBarIndicatorItem")
_UIStatusBarIndicatorLocationItem = _Class("_UIStatusBarIndicatorLocationItem")
_UIStatusBarElectronicTollCollectionItem = _Class(
    "_UIStatusBarElectronicTollCollectionItem"
)
_UIStatusBarRadarItem = _Class("_UIStatusBarRadarItem")
_UIStatusBarThermalItem = _Class("_UIStatusBarThermalItem")
_UIStatusBarIndicatorAlarmItem = _Class("_UIStatusBarIndicatorAlarmItem")
_UIStatusBarIndicatorCarPlayItem = _Class("_UIStatusBarIndicatorCarPlayItem")
_UIStatusBarIndicatorAirPlayItem = _Class("_UIStatusBarIndicatorAirPlayItem")
_UIStatusBarIndicatorVPNItem = _Class("_UIStatusBarIndicatorVPNItem")
_UIStatusBarIndicatorStudentItem = _Class("_UIStatusBarIndicatorStudentItem")
_UIStatusBarIndicatorAssistantItem = _Class("_UIStatusBarIndicatorAssistantItem")
_UIStatusBarIndicatorTTYItem = _Class("_UIStatusBarIndicatorTTYItem")
_UIStatusBarIndicatorAirplaneModeItem = _Class("_UIStatusBarIndicatorAirplaneModeItem")
_UIStatusBarIndicatorRotationLockItem = _Class("_UIStatusBarIndicatorRotationLockItem")
_UIStatusBarIndicatorLiquidDetectionItem = _Class(
    "_UIStatusBarIndicatorLiquidDetectionItem"
)
_UIStatusBarIndicatorQuietModeItem = _Class("_UIStatusBarIndicatorQuietModeItem")
_UIStatusBarBluetoothItem = _Class("_UIStatusBarBluetoothItem")
_UIStatusBarBackgroundActivityItem = _Class("_UIStatusBarBackgroundActivityItem")
_UIStatusBarFullBackgroundActivityItem = _Class(
    "_UIStatusBarFullBackgroundActivityItem"
)
_UIStatusBarPillBackgroundActivityItem = _Class(
    "_UIStatusBarPillBackgroundActivityItem"
)
_UIStatusBarVoiceControlItem = _Class("_UIStatusBarVoiceControlItem")
_UIStatusBarVoiceControlPillItem = _Class("_UIStatusBarVoiceControlPillItem")
_UITapticEngine = _Class("_UITapticEngine")
_UIFeedbackStateChangeConfiguration = _Class("_UIFeedbackStateChangeConfiguration")
UIPointerRegionRequest = _Class("UIPointerRegionRequest")
_UICursorRequest = _Class("_UICursorRequest")
UIRegion = _Class("UIRegion")
UIDynamicsDebug = _Class("UIDynamicsDebug")
UIDynamicItemGroup = _Class("UIDynamicItemGroup")
_UISearchControllerAnimator = _Class("_UISearchControllerAnimator")
_UISearchControllerTransplantSearchBarAnimator = _Class(
    "_UISearchControllerTransplantSearchBarAnimator"
)
_UISearchControllerOffscreenSearchBarAnimator = _Class(
    "_UISearchControllerOffscreenSearchBarAnimator"
)
_UISearchControllerInPlaceSearchBarAnimator = _Class(
    "_UISearchControllerInPlaceSearchBarAnimator"
)
_UISearchControllerCarPlaySearchBarAnimator = _Class(
    "_UISearchControllerCarPlaySearchBarAnimator"
)
_UISearchControllerATVSearchBarAnimator = _Class(
    "_UISearchControllerATVSearchBarAnimator"
)
_UISearchControllerATVSearchBarAnimatorLegacy = _Class(
    "_UISearchControllerATVSearchBarAnimatorLegacy"
)
UIDynamicAnimatorTicker = _Class("UIDynamicAnimatorTicker")
_UIDragSetDownAnimation = _Class("_UIDragSetDownAnimation")
_UIDataTransferMonitor = _Class("_UIDataTransferMonitor")
_UIDataTransferRequest = _Class("_UIDataTransferRequest")
_UIDruidDestinationConnection = _Class("_UIDruidDestinationConnection")
_UIDruidSourceConnection = _Class("_UIDruidSourceConnection")
_UIDraggingImageSlotOwner = _Class("_UIDraggingImageSlotOwner")
_UIInternalDraggingSessionDestination = _Class("_UIInternalDraggingSessionDestination")
_UIInternalDraggingSessionSource = _Class("_UIInternalDraggingSessionSource")
_UIDraggingImageComponent = _Class("_UIDraggingImageComponent")
_UIImageLoader = _Class("_UIImageLoader")
_UINSItemProviderImageLoader = _Class("_UINSItemProviderImageLoader")
_UINSURLRequestImageLoader = _Class("_UINSURLRequestImageLoader")
_UILoadingHandlerImageLoader = _Class("_UILoadingHandlerImageLoader")
_DUIAccessibilityDragStatus = _Class("_DUIAccessibilityDragStatus")
_DUIPotentialDrop = _Class("_DUIPotentialDrop")
_UIDropSessionImpl = _Class("_UIDropSessionImpl")
UISpringLoadedInteractionContextImpl = _Class("UISpringLoadedInteractionContextImpl")
_UIDropInteractionHighlightEffect = _Class("_UIDropInteractionHighlightEffect")
UIDropInteractionContextImpl = _Class("UIDropInteractionContextImpl")
_UIDragLiftEffectOperation = _Class("_UIDragLiftEffectOperation")
_UIDragLiftedItem = _Class("_UIDragLiftedItem")
UICollectionLayoutListConfiguration = _Class("UICollectionLayoutListConfiguration")
_UIDragAnimatingWrapper = _Class("_UIDragAnimatingWrapper")
_UIActiveTimer = _Class("_UIActiveTimer")
UIDocumentErrorRecoveryAttempter = _Class("UIDocumentErrorRecoveryAttempter")
UIDocumentAlertPresenter = _Class("UIDocumentAlertPresenter")
_UIArchiveExtractionController = _Class("_UIArchiveExtractionController")
_UIArchiveListingController = _Class("_UIArchiveListingController")
_UILibArchiveStreamingReader = _Class("_UILibArchiveStreamingReader")
_UILibArchiveStreamingExtractor = _Class("_UILibArchiveStreamingExtractor")
_UIArchiveItem = _Class("_UIArchiveItem")
_UILibArchiveItem = _Class("_UILibArchiveItem")
_UILibArchiveReaderLoadedItem = _Class("_UILibArchiveReaderLoadedItem")
_UILibArchiveAppleDoublePathSet = _Class("_UILibArchiveAppleDoublePathSet")
_UIDocumentPickerAuxiliaryOption = _Class("_UIDocumentPickerAuxiliaryOption")
_UISceneKeyboardProxyLayerForwardingStateMachine = _Class(
    "_UISceneKeyboardProxyLayerForwardingStateMachine"
)
UIKBFloatingKeyplaneTransformation = _Class("UIKBFloatingKeyplaneTransformation")
_UIModernSwitchVisualElementCacheKey = _Class("_UIModernSwitchVisualElementCacheKey")
_UISwitchSettings = _Class("_UISwitchSettings")
UISwitchMVEGestureTrackingSession = _Class("UISwitchMVEGestureTrackingSession")
UISegmentedControlSpringLoadedEffect = _Class("UISegmentedControlSpringLoadedEffect")
UISegmentedControlSpringLoadedBehavior = _Class(
    "UISegmentedControlSpringLoadedBehavior"
)
_UISegmentedControlSegmentHoverIdentifier = _Class(
    "_UISegmentedControlSegmentHoverIdentifier"
)
_UISegmentedControlAppearanceStorage = _Class("_UISegmentedControlAppearanceStorage")
_UIImageSystemImageCacheKey = _Class("_UIImageSystemImageCacheKey")
UIInputViewAnimationControllerViewControllerContext = _Class(
    "UIInputViewAnimationControllerViewControllerContext"
)
UIInputViewAnimationControllerViewController = _Class(
    "UIInputViewAnimationControllerViewController"
)
_UIApplicationModalProgressController = _Class("_UIApplicationModalProgressController")
_UIGestureStudyClickInteraction = _Class("_UIGestureStudyClickInteraction")
_UIAnimationCoordinator = _Class("_UIAnimationCoordinator")
_UIActionBridge = _Class("_UIActionBridge")
UIViewControllerPreviewAction = _Class("UIViewControllerPreviewAction")
UISplitViewControllerClassicImpl = _Class("UISplitViewControllerClassicImpl")
_UIPageControlInteractor = _Class("_UIPageControlInteractor")
_UISearchControllerDidScrollDelegate = _Class("_UISearchControllerDidScrollDelegate")
UISearchDisplayController = _Class("UISearchDisplayController")
_UIDictionaryManager = _Class("_UIDictionaryManager")
_UIDefinitionDictionary = _Class("_UIDefinitionDictionary")
_UIDefinitionValue = _Class("_UIDefinitionValue")
UIPreviewMenuItem = _Class("UIPreviewMenuItem")
_UIPageCurl = _Class("_UIPageCurl")
_UITransitionState = _Class("_UITransitionState")
_UIQueuingScrollViewState = _Class("_UIQueuingScrollViewState")
_UIPageCurlState = _Class("_UIPageCurlState")
_UISimpleTransitioningDelegate = _Class("_UISimpleTransitioningDelegate")
_UICollectionViewControllerLayoutToLayoutTransition = _Class(
    "_UICollectionViewControllerLayoutToLayoutTransition"
)
UIClientRotationContext = _Class("UIClientRotationContext")
_UINavigationCrossfadeAnimator = _Class("_UINavigationCrossfadeAnimator")
_UITabBarTVTransitioner = _Class("_UITabBarTVTransitioner")
_UIDiffableDataSourceSectionTransaction = _Class(
    "_UIDiffableDataSourceSectionTransaction"
)
_UIDiffableDataSourceTransaction = _Class("_UIDiffableDataSourceTransaction")
_UIPopoverAnimationController = _Class("_UIPopoverAnimationController")
_UIWindowSceneAccessibilityContrastSettingsDiffAction = _Class(
    "_UIWindowSceneAccessibilityContrastSettingsDiffAction"
)
_UIProgressiveBlurPresentationAnimator = _Class(
    "_UIProgressiveBlurPresentationAnimator"
)
_UIProgressiveBlurPresentationAnimationFactory = _Class(
    "_UIProgressiveBlurPresentationAnimationFactory"
)
_UIPreviewPlatterPanController = _Class("_UIPreviewPlatterPanController")
_UIActionSheetPresentationControllerVisualStyleiOS = _Class(
    "_UIActionSheetPresentationControllerVisualStyleiOS"
)
_UIPointerAssistantRegionID = _Class("_UIPointerAssistantRegionID")
_UIDatePickerCalendarTimeLabelStateMachineContext = _Class(
    "_UIDatePickerCalendarTimeLabelStateMachineContext"
)
UIPrinterAttributesService = _Class("UIPrinterAttributesService")
_UIDragMovementCadenceSettings = _Class("_UIDragMovementCadenceSettings")
_MapUpdate = _Class("_MapUpdate")
_UIDataSourceUpdateMap = _Class("_UIDataSourceUpdateMap")
_UIDataSourceSnapshot = _Class("_UIDataSourceSnapshot")
_UIDataSourceBatchUpdateMapHelper = _Class("_UIDataSourceBatchUpdateMapHelper")
_UICollectionViewSpringLoadedEffect = _Class("_UICollectionViewSpringLoadedEffect")
_UICollectionViewSpringLoadedBehavior = _Class("_UICollectionViewSpringLoadedBehavior")
_UICollectionViewSpringLoadedInteraction = _Class(
    "_UICollectionViewSpringLoadedInteraction"
)
_UICollectionViewPrefetchItem = _Class("_UICollectionViewPrefetchItem")
_UICollectionViewPrefetchingContext = _Class("_UICollectionViewPrefetchingContext")
_UICollectionViewDragSourceControllerDragState = _Class(
    "_UICollectionViewDragSourceControllerDragState"
)
_UICollectionViewSourcePrivateLocalObject = _Class(
    "_UICollectionViewSourcePrivateLocalObject"
)
_UICollectionViewDragSourceControllerSessionState = _Class(
    "_UICollectionViewDragSourceControllerSessionState"
)
_UICollectionViewDragSourceController = _Class("_UICollectionViewDragSourceController")
_UIDragDestinationControllerReorderingState = _Class(
    "_UIDragDestinationControllerReorderingState"
)
_UIDragDestinationControllerDropProposalState = _Class(
    "_UIDragDestinationControllerDropProposalState"
)
_UIDragDestinationControllerSessionState = _Class(
    "_UIDragDestinationControllerSessionState"
)
_UICollectionViewDragDestinationController = _Class(
    "_UICollectionViewDragDestinationController"
)
UICollectionViewPlaceholder = _Class("UICollectionViewPlaceholder")
UICollectionViewDropPlaceholder = _Class("UICollectionViewDropPlaceholder")
_UICollectionViewDropCoordinatorItem = _Class("_UICollectionViewDropCoordinatorItem")
_UICollectionViewCellAppearanceState = _Class("_UICollectionViewCellAppearanceState")
_UICollectionViewDropItem = _Class("_UICollectionViewDropItem")
_UICollectionViewPlaceholderContext = _Class("_UICollectionViewPlaceholderContext")
_UIDropAnimationHandlers = _Class("_UIDropAnimationHandlers")
UICollectionViewReorderedItem = _Class("UICollectionViewReorderedItem")
UICollectionViewAnimation = _Class("UICollectionViewAnimation")
_UICollectionViewTrackedValue = _Class("_UICollectionViewTrackedValue")
_UICollectionViewTrackedValueItem = _Class("_UICollectionViewTrackedValueItem")
_UICollectionViewItemKey = _Class("_UICollectionViewItemKey")
UICollectionViewUpdate = _Class("UICollectionViewUpdate")
UICollectionViewUpdateItem = _Class("UICollectionViewUpdateItem")
_UICollectionViewCellPromiseRegion = _Class("_UICollectionViewCellPromiseRegion")
UIAutoRespondingScrollViewControllerKeyboardSupport = _Class(
    "UIAutoRespondingScrollViewControllerKeyboardSupport"
)
UICellHighlightingSupport = _Class("UICellHighlightingSupport")
UITableViewCellUnhighlightedState = _Class("UITableViewCellUnhighlightedState")
UIContextualAction = _Class("UIContextualAction")
UISwipeAction = _Class("UISwipeAction")
UICollectionViewTableLayoutSwipeAction = _Class(
    "UICollectionViewTableLayoutSwipeAction"
)
_UIContextMenuCommitAnimation = _Class("_UIContextMenuCommitAnimation")
_UIContextMenuActionsListSection = _Class("_UIContextMenuActionsListSection")
_UIDataSourceSnapshotter = _Class("_UIDataSourceSnapshotter")
_UICollectionViewListSnapshotter = _Class("_UICollectionViewListSnapshotter")
_UICollectionViewListSeparatorDiff = _Class("_UICollectionViewListSeparatorDiff")
_UICollectionViewListLayoutVisualProvider = _Class(
    "_UICollectionViewListLayoutVisualProvider"
)
_UICollectionViewListLayoutVisualProvider_tvOS = _Class(
    "_UICollectionViewListLayoutVisualProvider_tvOS"
)
_UICollectionViewListLayoutVisualProvider_iOS = _Class(
    "_UICollectionViewListLayoutVisualProvider_iOS"
)
_UICollectionViewListCellVisualProvider = _Class(
    "_UICollectionViewListCellVisualProvider"
)
_UICollectionViewListCellVisualProvider_tvOS = _Class(
    "_UICollectionViewListCellVisualProvider_tvOS"
)
_UICollectionViewListCellVisualProvider_iOS = _Class(
    "_UICollectionViewListCellVisualProvider_iOS"
)
_UIIdentifierDifferMovePair = _Class("_UIIdentifierDifferMovePair")
_UIIdentifierDiffer = _Class("_UIIdentifierDiffer")
_UIDiffableDataSourceViewUpdater = _Class("_UIDiffableDataSourceViewUpdater")
_UIDiffableDataSourceDiffer = _Class("_UIDiffableDataSourceDiffer")
__UIDiffableDataSource = _Class("__UIDiffableDataSource")
__UIDiffableDataSourceSnapshot = _Class("__UIDiffableDataSourceSnapshot")
UITableViewDiffableDataSource = _Class("UITableViewDiffableDataSource")
UICollectionViewDiffableDataSource = _Class("UICollectionViewDiffableDataSource")
NSDiffableDataSourceSnapshot = _Class("NSDiffableDataSourceSnapshot")
_UIRTree = _Class("_UIRTree")
_UIOrderedRangeIndexer = _Class("_UIOrderedRangeIndexer")
_UICollectionLayoutAuxillaryItemSolver = _Class(
    "_UICollectionLayoutAuxillaryItemSolver"
)
_UICollectionLayoutSupplementaryEnrollment = _Class(
    "_UICollectionLayoutSupplementaryEnrollment"
)
_UICollectionLayoutSupplementaryRegistrar = _Class(
    "_UICollectionLayoutSupplementaryRegistrar"
)
_UICollectionLayoutSolveParameters = _Class("_UICollectionLayoutSolveParameters")
_UICollectionLayoutSolveResult = _Class("_UICollectionLayoutSolveResult")
_UICollectionLayoutSectionFixedSolver = _Class("_UICollectionLayoutSectionFixedSolver")
_UICollectionLayoutSolutionState = _Class("_UICollectionLayoutSolutionState")
_UICollectionEstimatedSolutionBookmark = _Class(
    "_UICollectionEstimatedSolutionBookmark"
)
_UICollectionLayoutSectionEstimatedSolver = _Class(
    "_UICollectionLayoutSectionEstimatedSolver"
)
_UICollectionLayoutItemSolverState = _Class("_UICollectionLayoutItemSolverState")
_UICollectionAvailableDimensionalLayoutSpace = _Class(
    "_UICollectionAvailableDimensionalLayoutSpace"
)
_UICollectionSolutionGroupArrangementItem = _Class(
    "_UICollectionSolutionGroupArrangementItem"
)
_UICollectionEdgeSpacingSolution = _Class("_UICollectionEdgeSpacingSolution")
_UICollectionLayoutItemSolver = _Class("_UICollectionLayoutItemSolver")
_UIContentInsetsEnvironment = _Class("_UIContentInsetsEnvironment")
_UICollectionLayoutFramesQueryResultElementIndexKey = _Class(
    "_UICollectionLayoutFramesQueryResultElementIndexKey"
)
_UICollectionLayoutAuxillaryKey = _Class("_UICollectionLayoutAuxillaryKey")
_UICollectionLayoutSectionGeometryTranslator = _Class(
    "_UICollectionLayoutSectionGeometryTranslator"
)
_UICollectionLayoutAuxillaryOffsets = _Class("_UICollectionLayoutAuxillaryOffsets")
_UICollectionLayoutFramesQueryResult = _Class("_UICollectionLayoutFramesQueryResult")
_UICollectionLayoutDynamicsConfiguration = _Class(
    "_UICollectionLayoutDynamicsConfiguration"
)
NSCollectionLayoutVisibleItem = _Class("NSCollectionLayoutVisibleItem")
_UICollectionLayoutVisualFormatTreeParser = _Class(
    "_UICollectionLayoutVisualFormatTreeParser"
)
_UICollectionLayoutVisualFormatItem = _Class("_UICollectionLayoutVisualFormatItem")
_UICollectionLayoutVisualTreeNode = _Class("_UICollectionLayoutVisualTreeNode")
_UICollectionLayoutVisualFormatParser = _Class("_UICollectionLayoutVisualFormatParser")
_UICollectionLayoutVFLParserItem = _Class("_UICollectionLayoutVFLParserItem")
_UICollectionLayoutFramesQueryOffsets = _Class("_UICollectionLayoutFramesQueryOffsets")
NSCollectionLayoutEnvironment = _Class("NSCollectionLayoutEnvironment")
_UICollectionLayoutContainer = _Class("_UICollectionLayoutContainer")
_UICollectionViewLayoutOrthogonalScrollingSectionState = _Class(
    "_UICollectionViewLayoutOrthogonalScrollingSectionState"
)
_UICollectionCompositionalLayoutSolverRestorableState = _Class(
    "_UICollectionCompositionalLayoutSolverRestorableState"
)
_UICollectionCompositionalLayoutSolverBookmarkStateSnapshotter = _Class(
    "_UICollectionCompositionalLayoutSolverBookmarkStateSnapshotter"
)
_UICollectionCompositionalLayoutSolverOptions = _Class(
    "_UICollectionCompositionalLayoutSolverOptions"
)
_UICollectionCompositionalSolverPreferredSizesRebaseInfo = _Class(
    "_UICollectionCompositionalSolverPreferredSizesRebaseInfo"
)
_UICollectionCompositionalLayoutSolverResolveResult = _Class(
    "_UICollectionCompositionalLayoutSolverResolveResult"
)
_UICollectionCompositionalLayoutSolverUpdate = _Class(
    "_UICollectionCompositionalLayoutSolverUpdate"
)
_UICollectionSectionSolutionBookmark = _Class("_UICollectionSectionSolutionBookmark")
_UICollectionLayoutUpdateContainerOffsetResult = _Class(
    "_UICollectionLayoutUpdateContainerOffsetResult"
)
UIDynamicBehavior = _Class("UIDynamicBehavior")
_UISpringBehavior = _Class("_UISpringBehavior")
_UIPlatterMenuSnapBehavior = _Class("_UIPlatterMenuSnapBehavior")
UISnapBehavior = _Class("UISnapBehavior")
UIPushBehavior = _Class("UIPushBehavior")
UIGravityBehavior = _Class("UIGravityBehavior")
UIFieldBehavior = _Class("UIFieldBehavior")
UIDynamicItemBehavior = _Class("UIDynamicItemBehavior")
_UIDynamicItemObservingBehavior = _Class("_UIDynamicItemObservingBehavior")
UICollisionBehavior = _Class("UICollisionBehavior")
UIAttachmentBehavior = _Class("UIAttachmentBehavior")
_UICollectionCompositionalLayoutDynamicBehavior = _Class(
    "_UICollectionCompositionalLayoutDynamicBehavior"
)
UIDynamicAnimator = _Class("UIDynamicAnimator")
_UICollectionCompositionalLayoutDynamicAnimator = _Class(
    "_UICollectionCompositionalLayoutDynamicAnimator"
)
_UICollectionCompositionalLayoutSolver = _Class(
    "_UICollectionCompositionalLayoutSolver"
)
_UIASCIIArtFramesRenderer = _Class("_UIASCIIArtFramesRenderer")
UICollectionViewCompositionalLayoutConfiguration = _Class(
    "UICollectionViewCompositionalLayoutConfiguration"
)
_UICollectionPreferredSizes = _Class("_UICollectionPreferredSizes")
_UICollectionPreferredSize = _Class("_UICollectionPreferredSize")
NSCollectionLayoutAnchor = _Class("NSCollectionLayoutAnchor")
NSCollectionLayoutSize = _Class("NSCollectionLayoutSize")
NSCollectionLayoutDimension = _Class("NSCollectionLayoutDimension")
NSCollectionLayoutEdgeSpacing = _Class("NSCollectionLayoutEdgeSpacing")
NSCollectionLayoutSpacing = _Class("NSCollectionLayoutSpacing")
NSCollectionLayoutSection = _Class("NSCollectionLayoutSection")
_UICollectionViewListLayoutSection = _Class("_UICollectionViewListLayoutSection")
NSCollectionLayoutGroupCustomItem = _Class("NSCollectionLayoutGroupCustomItem")
NSCollectionLayoutItem = _Class("NSCollectionLayoutItem")
NSCollectionLayoutDecorationItem = _Class("NSCollectionLayoutDecorationItem")
NSCollectionLayoutSupplementaryItem = _Class("NSCollectionLayoutSupplementaryItem")
NSCollectionLayoutBoundarySupplementaryItem = _Class(
    "NSCollectionLayoutBoundarySupplementaryItem"
)
NSCollectionLayoutGroup = _Class("NSCollectionLayoutGroup")
_UIDatePickerCalendarMonthSet = _Class("_UIDatePickerCalendarMonthSet")
_UICollectionViewOutlineCellDisclosureConfiguration = _Class(
    "_UICollectionViewOutlineCellDisclosureConfiguration"
)
_UIClickPresentation = _Class("_UIClickPresentation")
_UIContextMenuPresentation = _Class("_UIContextMenuPresentation")
_UIWindowSceneLifecycleSettingsDiffAction = _Class(
    "_UIWindowSceneLifecycleSettingsDiffAction"
)
_UICanvasSceneLaunchOptions = _Class("_UICanvasSceneLaunchOptions")
_UIPackedRegion = _Class("_UIPackedRegion")
_UIAlignmentRegion = _Class("_UIAlignmentRegion")
_UISimplex = _Class("_UISimplex")
_UIHyperrepeatedRegion = _Class("_UIHyperrepeatedRegion")
_UIHypersphere = _Class("_UIHypersphere")
_UIHyperplane = _Class("_UIHyperplane")
_UICellAccessoryConfiguration = _Class("_UICellAccessoryConfiguration")
_UICellAccessoryConfigurationCustomView = _Class(
    "_UICellAccessoryConfigurationCustomView"
)
_UICellAccessoryConfigurationBadge = _Class("_UICellAccessoryConfigurationBadge")
_UICellAccessoryConfigurationSeparator = _Class(
    "_UICellAccessoryConfigurationSeparator"
)
_UICellAccessoryConfigurationOutlineDisclosure = _Class(
    "_UICellAccessoryConfigurationOutlineDisclosure"
)
_UICellAccessoryConfigurationMultiselect = _Class(
    "_UICellAccessoryConfigurationMultiselect"
)
_UICellAccessoryConfigurationReorder = _Class("_UICellAccessoryConfigurationReorder")
_UICellAccessoryConfigurationInsert = _Class("_UICellAccessoryConfigurationInsert")
_UICellAccessoryConfigurationDelete = _Class("_UICellAccessoryConfigurationDelete")
_UICellAccessoryConfigurationCheckmark = _Class(
    "_UICellAccessoryConfigurationCheckmark"
)
_UICellAccessoryConfigurationDisclosureIndicator = _Class(
    "_UICellAccessoryConfigurationDisclosureIndicator"
)
_UIBadgeVisualStyle = _Class("_UIBadgeVisualStyle")
_UIBadgeTVVisualStyle = _Class("_UIBadgeTVVisualStyle")
_UIBadgeCarplayVisualStyle = _Class("_UIBadgeCarplayVisualStyle")
_UIBadgePhonePadVisualStyle = _Class("_UIBadgePhonePadVisualStyle")
_UIBadgePadHorizontalVisualStyle = _Class("_UIBadgePadHorizontalVisualStyle")
_UIBadgePhoneLandscapeVisualStyle = _Class("_UIBadgePhoneLandscapeVisualStyle")
_UISceneKeyboardProxyLayerForwardingManager = _Class(
    "_UISceneKeyboardProxyLayerForwardingManager"
)
_UICommandIdentifier = _Class("_UICommandIdentifier")
_UITabBarVisualProvider = _Class("_UITabBarVisualProvider")
_UITabBarVisualProviderLegacyTVOS = _Class("_UITabBarVisualProviderLegacyTVOS")
_UITabBarVisualProviderLegacyIOS = _Class("_UITabBarVisualProviderLegacyIOS")
_UINullClickHighlightEffect = _Class("_UINullClickHighlightEffect")
UITabBarItemProxy = _Class("UITabBarItemProxy")
_UITabBarAppearanceStorage = _Class("_UITabBarAppearanceStorage")
_UISearchBarVisualProviderLegacy = _Class("_UISearchBarVisualProviderLegacy")
_UISearchBarTransitionContext = _Class("_UISearchBarTransitionContext")
_UISearchBarTransitionerBase = _Class("_UISearchBarTransitionerBase")
_UISearchBarTokenOptionsPresentationTransitioner = _Class(
    "_UISearchBarTokenOptionsPresentationTransitioner"
)
_UISearchBarTokenOptionsDismissalTransitioner = _Class(
    "_UISearchBarTokenOptionsDismissalTransitioner"
)
_UISearchBarSearchPresentationTransitioner = _Class(
    "_UISearchBarSearchPresentationTransitioner"
)
_UISearchBarSearchDismissalTransitioner = _Class(
    "_UISearchBarSearchDismissalTransitioner"
)
_UISearchBarAppearanceStorage = _Class("_UISearchBarAppearanceStorage")
_UISearchBarBackgroundCacheKey = _Class("_UISearchBarBackgroundCacheKey")
_UINavigationBarTransitionContext = _Class("_UINavigationBarTransitionContext")
_UINavigationBarTransitionContextDismissSearch = _Class(
    "_UINavigationBarTransitionContextDismissSearch"
)
_UINavigationBarTransitionContextPresentSearch = _Class(
    "_UINavigationBarTransitionContextPresentSearch"
)
_UINavigationBarTransitionContextCrossfade = _Class(
    "_UINavigationBarTransitionContextCrossfade"
)
_UINavigationBarTransitionContextPop = _Class("_UINavigationBarTransitionContextPop")
_UINavigationBarTransitionContextPush = _Class("_UINavigationBarTransitionContextPush")
_UINavigationBarLargeTitleCandidate = _Class("_UINavigationBarLargeTitleCandidate")
_UIFocusActiveSceneObserver = _Class("_UIFocusActiveSceneObserver")
_UINavigationBarTransitionAssistant = _Class("_UINavigationBarTransitionAssistant")
_UINavigationBarGestureHandler = _Class("_UINavigationBarGestureHandler")
_UINavigationBarTitleViewOverlayRects = _Class("_UINavigationBarTitleViewOverlayRects")
_UINavigationBarContents = _Class("_UINavigationBarContents")
_UIBarItemAppearanceStorage = _Class("_UIBarItemAppearanceStorage")
_UITabBarItemAppearanceStorage = _Class("_UITabBarItemAppearanceStorage")
_UIBarButtonItemAppearanceStorage = _Class("_UIBarButtonItemAppearanceStorage")
_UIBarBackButtonItemAppearanceStorage = _Class("_UIBarBackButtonItemAppearanceStorage")
_UIStretchableShadow = _Class("_UIStretchableShadow")
_UIVisualEffectDifferenceEngine = _Class("_UIVisualEffectDifferenceEngine")
_UILegacyEffectConverter = _Class("_UILegacyEffectConverter")
_UILegacyEffectConverterTVOS = _Class("_UILegacyEffectConverterTVOS")
_UILegacyEffectConverterIOS = _Class("_UILegacyEffectConverterIOS")
_UIVisualEffectConfig = _Class("_UIVisualEffectConfig")
_UIVisualEffectLayerConfig = _Class("_UIVisualEffectLayerConfig")
_UIVisualEffectVibrantLayerConfig = _Class("_UIVisualEffectVibrantLayerConfig")
_UIVisualEffectTintLayerConfig = _Class("_UIVisualEffectTintLayerConfig")
_UIBasicHeaderFooterContentViewConfiguration = _Class(
    "_UIBasicHeaderFooterContentViewConfiguration"
)
UIActivityItemsConfiguration = _Class("UIActivityItemsConfiguration")
_UITextInteractableItem = _Class("_UITextInteractableItem")
_UITextInteractableLink = _Class("_UITextInteractableLink")
_UITextInteractableAttachment = _Class("_UITextInteractableAttachment")
_UIBackdropColorSettings = _Class("_UIBackdropColorSettings")
_UIActionGroup = _Class("_UIActionGroup")
_UIContextMenuPreviewActionGroup = _Class("_UIContextMenuPreviewActionGroup")
_UIAction = _Class("_UIAction")
_UIBackdropViewSettings = _Class("_UIBackdropViewSettings")
_UIBackdropViewSettingsATVTabBarLight = _Class("_UIBackdropViewSettingsATVTabBarLight")
_UIBackdropViewSettingsATVTabBarDark = _Class("_UIBackdropViewSettingsATVTabBarDark")
_UIBackdropViewSettingsCombiner = _Class("_UIBackdropViewSettingsCombiner")
_UIBackdropViewSettingsColorSample = _Class("_UIBackdropViewSettingsColorSample")
_UIBackdropViewSettingsBlur = _Class("_UIBackdropViewSettingsBlur")
_UIBackdropViewSettingsReplicator = _Class("_UIBackdropViewSettingsReplicator")
_UIBackdropViewSettingsNone = _Class("_UIBackdropViewSettingsNone")
_UIBackdropViewSettingsLightKeyboard = _Class("_UIBackdropViewSettingsLightKeyboard")
_UIBackdropViewSettingsLightEmojiKeyboard = _Class(
    "_UIBackdropViewSettingsLightEmojiKeyboard"
)
_UIBackdropViewSettingsUltraLight = _Class("_UIBackdropViewSettingsUltraLight")
_UIBackdropViewSettingsUltraColored = _Class("_UIBackdropViewSettingsUltraColored")
_UIBackdropViewSettingsNonAdaptive = _Class("_UIBackdropViewSettingsNonAdaptive")
_UIBackdropViewSettingsUltraDark = _Class("_UIBackdropViewSettingsUltraDark")
_UIBackdropViewSettingsUltraDarkWithZoom = _Class(
    "_UIBackdropViewSettingsUltraDarkWithZoom"
)
_UIBackdropViewSettingsLight = _Class("_UIBackdropViewSettingsLight")
_UIBackdropViewSettingsFlatSemiLight = _Class("_UIBackdropViewSettingsFlatSemiLight")
_UIBackdropViewSettingsSemiLight = _Class("_UIBackdropViewSettingsSemiLight")
_UIBackdropViewSettingsAdaptiveLight = _Class("_UIBackdropViewSettingsAdaptiveLight")
_UIBackdropViewSettingsLightLow = _Class("_UIBackdropViewSettingsLightLow")
_UIBackdropViewSettingsDark = _Class("_UIBackdropViewSettingsDark")
_UIBackdropViewSettingsPasscodePaddle = _Class("_UIBackdropViewSettingsPasscodePaddle")
_UIBackdropViewSettingsDarkWithZoom = _Class("_UIBackdropViewSettingsDarkWithZoom")
_UIBackdropViewSettingsDarkLow = _Class("_UIBackdropViewSettingsDarkLow")
_UIBackdropViewSettingsColored = _Class("_UIBackdropViewSettingsColored")
_UIBackdropViewSettingsATVUltraLight = _Class("_UIBackdropViewSettingsATVUltraLight")
_UIBackdropViewSettingsATVUltraDark = _Class("_UIBackdropViewSettingsATVUltraDark")
_UIBackdropViewSettingsATVSemiLight = _Class("_UIBackdropViewSettingsATVSemiLight")
_UIBackdropViewSettingsATVSemiDark = _Class("_UIBackdropViewSettingsATVSemiDark")
_UIBackdropViewSettingsATVMenuLight = _Class("_UIBackdropViewSettingsATVMenuLight")
_UIBackdropViewSettingsATVMenuDark = _Class("_UIBackdropViewSettingsATVMenuDark")
_UIBackdropViewSettingsATVMediumLight = _Class("_UIBackdropViewSettingsATVMediumLight")
_UIBackdropViewSettingsATVMediumDark = _Class("_UIBackdropViewSettingsATVMediumDark")
_UIBackdropViewSettingsATVLight = _Class("_UIBackdropViewSettingsATVLight")
_UIBackdropViewSettingsATVDark = _Class("_UIBackdropViewSettingsATVDark")
_UIBackdropViewSettingsATVAdaptiveLighten = _Class(
    "_UIBackdropViewSettingsATVAdaptiveLighten"
)
_UIBackdropViewSettingsATVAdaptive = _Class("_UIBackdropViewSettingsATVAdaptive")
_UIBackdropViewSettingsATVAccessoryLight = _Class(
    "_UIBackdropViewSettingsATVAccessoryLight"
)
_UIBackdropViewSettingsATVAccessoryDark = _Class(
    "_UIBackdropViewSettingsATVAccessoryDark"
)
UIAvoidanceCoordinator = _Class("UIAvoidanceCoordinator")
UIAvoidanceLargestArea = _Class("UIAvoidanceLargestArea")
_UIViewPropertyAnimatorTrackingGroup = _Class("_UIViewPropertyAnimatorTrackingGroup")
UICubicTimingParameters = _Class("UICubicTimingParameters")
_UIViewCubicTimingFunction = _Class("_UIViewCubicTimingFunction")
_UIViewPropertyAnimationDescription = _Class("_UIViewPropertyAnimationDescription")
_UIViewPropertyAnimationUpdate = _Class("_UIViewPropertyAnimationUpdate")
_UIDynamicAnimationActiveValue = _Class("_UIDynamicAnimationActiveValue")
_UIFocusGroupDescriptorStringIdentifier = _Class(
    "_UIFocusGroupDescriptorStringIdentifier"
)
_UIFocusGroupDescriptor = _Class("_UIFocusGroupDescriptor")
_UIDynamicAnimation = _Class("_UIDynamicAnimation")
_UIDynamicValueConvergenceAnimation = _Class("_UIDynamicValueConvergenceAnimation")
_UIDynamicAnimationGroup = _Class("_UIDynamicAnimationGroup")
_UIDynamicValueAnimation = _Class("_UIDynamicValueAnimation")
_UIDynamicAnimationState = _Class("_UIDynamicAnimationState")
_UIRapidClickPresentationAssistant = _Class("_UIRapidClickPresentationAssistant")
_UIAlertControllerVisualStyleAlertTVCustomCurveFactory = _Class(
    "_UIAlertControllerVisualStyleAlertTVCustomCurveFactory"
)
UIInputViewPostPinningReloadState = _Class("UIInputViewPostPinningReloadState")
_UITextPlainLinkInteractionHandler = _Class("_UITextPlainLinkInteractionHandler")
_UITextDataDetectedLinkInteractionHandler = _Class(
    "_UITextDataDetectedLinkInteractionHandler"
)
_UITextAttachmentInteractionHandler = _Class("_UITextAttachmentInteractionHandler")
_UICollectionLayoutSectionListSolver = _Class("_UICollectionLayoutSectionListSolver")
UIInterfaceActionRepresentationViewSpringLoadedEffect = _Class(
    "UIInterfaceActionRepresentationViewSpringLoadedEffect"
)
UIInterfaceActionRepresentationViewSpringLoadedBehavior = _Class(
    "UIInterfaceActionRepresentationViewSpringLoadedBehavior"
)
UIInterfaceActionSeparatorAttributes = _Class("UIInterfaceActionSeparatorAttributes")
UIInterfaceActionHighlightAttributes = _Class("UIInterfaceActionHighlightAttributes")
_UISceneCanvasComponent = _Class("_UISceneCanvasComponent")
_UISceneCanvasSceneActionsHandler = _Class("_UISceneCanvasSceneActionsHandler")
_UISceneCanvasSettingsDiffAction = _Class("_UISceneCanvasSettingsDiffAction")
_UIInterfaceActionRepresentationViewContext_AppleTV = _Class(
    "_UIInterfaceActionRepresentationViewContext_AppleTV"
)
_UIAlertControllerShimPresenter = _Class("_UIAlertControllerShimPresenter")
UIAutonomousSingleAppModeSession = _Class("UIAutonomousSingleAppModeSession")
UIAutonomousSingleAppModeConfiguration = _Class(
    "UIAutonomousSingleAppModeConfiguration"
)
UIAccessibilityHUDLayoutManager = _Class("UIAccessibilityHUDLayoutManager")
UIAccessibilityCustomViewHUDLayoutManager = _Class(
    "UIAccessibilityCustomViewHUDLayoutManager"
)
UIAccessibilityImageOnlyHUDLayoutManager = _Class(
    "UIAccessibilityImageOnlyHUDLayoutManager"
)
UIAccessibilityLabelOnlyHUDLayoutManager = _Class(
    "UIAccessibilityLabelOnlyHUDLayoutManager"
)
UIAccessibilityHUDItem = _Class("UIAccessibilityHUDItem")
UIAccessibilityHUDPositionManager = _Class("UIAccessibilityHUDPositionManager")
_UICustomScheduleController = _Class("_UICustomScheduleController")
UIAccessibilityContainerReferenceHolder = _Class(
    "UIAccessibilityContainerReferenceHolder"
)
_UIDiffableDataSourceSectionSnapshotRebaser = _Class(
    "_UIDiffableDataSourceSectionSnapshotRebaser"
)
_UIContextMenuStyle = _Class("_UIContextMenuStyle")
_UISearchTokenAttachmentViewProvider = _Class("_UISearchTokenAttachmentViewProvider")
_UIApplicationInfo = _Class("_UIApplicationInfo")
UIWillPresentNotificationActionResponse = _Class(
    "UIWillPresentNotificationActionResponse"
)
UIWatchKitExtensionRequestActionResponse = _Class(
    "UIWatchKitExtensionRequestActionResponse"
)
UISceneProposalActionResponse = _Class("UISceneProposalActionResponse")
UISceneHitTestActionResponse = _Class("UISceneHitTestActionResponse")
UIDestroySceneActionResponse = _Class("UIDestroySceneActionResponse")
UIFetchContentInBackgroundActionResponse = _Class(
    "UIFetchContentInBackgroundActionResponse"
)
UIIntentForwardingActionResponse = _Class("UIIntentForwardingActionResponse")
PKExtendedPhysicsWorld = _Class("PKExtendedPhysicsWorld")
PKExtendedPhysicsBody = _Class("PKExtendedPhysicsBody")
_UIConstantConstraintSet = _Class("_UIConstantConstraintSet")
_UIFlexibleConstantConstraintSet = _Class("_UIFlexibleConstantConstraintSet")
_UIVisualEffectViewEntry = _Class("_UIVisualEffectViewEntry")
_UIWallpaperEffectEntry = _Class("_UIWallpaperEffectEntry")
_UICopyEffectViewEntry = _Class("_UICopyEffectViewEntry")
_UIVisualEffectAlphaEntry = _Class("_UIVisualEffectAlphaEntry")
_UIVisualEffectViewTransitioningEntry = _Class("_UIVisualEffectViewTransitioningEntry")
_UIVisualEffectViewReversingEntry = _Class("_UIVisualEffectViewReversingEntry")
_UICompositingEffectViewEntry = _Class("_UICompositingEffectViewEntry")
_UIOverlayEffectViewEntry = _Class("_UIOverlayEffectViewEntry")
_UIZoomEffectViewEntry = _Class("_UIZoomEffectViewEntry")
_UITintColorViewEntry = _Class("_UITintColorViewEntry")
_UIVibrancyEffectImpl = _Class("_UIVibrancyEffectImpl")
_UIVibrancyEffectVibrantColorMatrixImpl = _Class(
    "_UIVibrancyEffectVibrantColorMatrixImpl"
)
_UIVibrancyEffectModernCompositedImpl = _Class("_UIVibrancyEffectModernCompositedImpl")
_UIVibrancyEffectModernVibrancyImpl = _Class("_UIVibrancyEffectModernVibrancyImpl")
_UIVibrancyEffectLegacyImpl = _Class("_UIVibrancyEffectLegacyImpl")
_UIVibrancyEffectCoreMaterialImpl = _Class("_UIVibrancyEffectCoreMaterialImpl")
_UIInterfaceActionSeparatorConstraintController = _Class(
    "_UIInterfaceActionSeparatorConstraintController"
)
UIAlertVisualStyleUpdatableConstraints = _Class(
    "UIAlertVisualStyleUpdatableConstraints"
)
_UIAlertControllerActionViewMetrics = _Class("_UIAlertControllerActionViewMetrics")
UIInterfaceAction = _Class("UIInterfaceAction")
_UIAlertControllerActionViewInterfaceAction = _Class(
    "_UIAlertControllerActionViewInterfaceAction"
)
UIInterfaceActionSelectionTrackingController = _Class(
    "UIInterfaceActionSelectionTrackingController"
)
UIInterfaceActionSection = _Class("UIInterfaceActionSection")
UIInterfaceActionGroup = _Class("UIInterfaceActionGroup")
_UIAlertControllerAnimatedTransitioning = _Class(
    "_UIAlertControllerAnimatedTransitioning"
)
UIInterfaceActionVisualStyleViewState = _Class("UIInterfaceActionVisualStyleViewState")
UIInterfaceActionViewState = _Class("UIInterfaceActionViewState")
UIInterfaceActionGroupViewState = _Class("UIInterfaceActionGroupViewState")
UIInterfaceActionConcreteVisualStyle = _Class("UIInterfaceActionConcreteVisualStyle")
UIInterfaceActionConcreteVisualStyle_CarPlay = _Class(
    "UIInterfaceActionConcreteVisualStyle_CarPlay"
)
UIInterfaceActionConcreteVisualStyle_CarPlayAlert = _Class(
    "UIInterfaceActionConcreteVisualStyle_CarPlayAlert"
)
UIInterfaceActionConcreteVisualStyle_AppleTV = _Class(
    "UIInterfaceActionConcreteVisualStyle_AppleTV"
)
UIInterfaceActionConcreteVisualStyleAlert_AppleTVAlert = _Class(
    "UIInterfaceActionConcreteVisualStyleAlert_AppleTVAlert"
)
UIInterfaceActionConcreteVisualStyle_iOS = _Class(
    "UIInterfaceActionConcreteVisualStyle_iOS"
)
UIInterfaceActionConcreteVisualStyle_iOSSheet = _Class(
    "UIInterfaceActionConcreteVisualStyle_iOSSheet"
)
UIInterfaceActionConcreteVisualStylePreviewPlatter = _Class(
    "UIInterfaceActionConcreteVisualStylePreviewPlatter"
)
UIInterfaceActionConcreteVisualStyle_iOSInlineActionSheet = _Class(
    "UIInterfaceActionConcreteVisualStyle_iOSInlineActionSheet"
)
UIInterfaceActionConcreteVisualStyle_iOSActivitySheet = _Class(
    "UIInterfaceActionConcreteVisualStyle_iOSActivitySheet"
)
UIInterfaceActionConcreteVisualStyle_iOSAlert = _Class(
    "UIInterfaceActionConcreteVisualStyle_iOSAlert"
)
UIInterfaceActionConcreteVisualStyleFactory_CarPlay = _Class(
    "UIInterfaceActionConcreteVisualStyleFactory_CarPlay"
)
UIInterfaceActionConcreteVisualStyleFactory_AppleTV = _Class(
    "UIInterfaceActionConcreteVisualStyleFactory_AppleTV"
)
UIInterfaceActionConcreteVisualStyleFactory_iOS = _Class(
    "UIInterfaceActionConcreteVisualStyleFactory_iOS"
)
UIInterfaceActionVisualStyle = _Class("UIInterfaceActionVisualStyle")
UIInterfaceActionOverrideVisualStyle = _Class("UIInterfaceActionOverrideVisualStyle")
UIAlertControllerVisualStyle = _Class("UIAlertControllerVisualStyle")
UIAlertControllerVisualStyleActionSheet = _Class(
    "UIAlertControllerVisualStyleActionSheet"
)
UIAlertControllerVisualStyleActionSheetInline = _Class(
    "UIAlertControllerVisualStyleActionSheetInline"
)
UIAlertControllerVisualStyleActionSheetCar = _Class(
    "UIAlertControllerVisualStyleActionSheetCar"
)
UIAlertControllerVisualStyleAlert = _Class("UIAlertControllerVisualStyleAlert")
UIAlertControllerVisualStyleAlertTV = _Class("UIAlertControllerVisualStyleAlertTV")
UIAlertControllerVisualStyleAlertCar = _Class("UIAlertControllerVisualStyleAlertCar")
UIAlertControllerDescriptor = _Class("UIAlertControllerDescriptor")
_UIAlertControllerTransitioningDelegate = _Class(
    "_UIAlertControllerTransitioningDelegate"
)
_UISceneSettingsMediaTimingAnimationFactory = _Class(
    "_UISceneSettingsMediaTimingAnimationFactory"
)
NSDocumentDifferenceSizeTriple = _Class("NSDocumentDifferenceSizeTriple")
UITextPasteItem = _Class("UITextPasteItem")
_UISearchTextFieldPasteItem = _Class("_UISearchTextFieldPasteItem")
_UITextPasteSession = _Class("_UITextPasteSession")
UITextPasteCoordinator = _Class("UITextPasteCoordinator")
UITextInputArrowKeyHistory = _Class("UITextInputArrowKeyHistory")
_UIPasteboardOptions = _Class("_UIPasteboardOptions")
UIPasteboardOptions = _Class("UIPasteboardOptions")
UIAutoscroll = _Class("UIAutoscroll")
_UIAssertionRecord = _Class("_UIAssertionRecord")
_UIAssertionBase = _Class("_UIAssertionBase")
UITextSelectionWindowAveragedValue = _Class("UITextSelectionWindowAveragedValue")
UITextGestureTuning = _Class("UITextGestureTuning")
_UIKitDragAndDropStatistics = _Class("_UIKitDragAndDropStatistics")
UIDragInteractionContextImpl = _Class("UIDragInteractionContextImpl")
_DUIDirtyItem = _Class("_DUIDirtyItem")
_DUIVisibleDroppedItem = _Class("_DUIVisibleDroppedItem")
_DUIImageComponent = _Class("_DUIImageComponent")
_DUIPreview = _Class("_DUIPreview")
_DUIPreviewAndImageComponent = _Class("_DUIPreviewAndImageComponent")
UIDraggingSessionConfiguration = _Class("UIDraggingSessionConfiguration")
UIDraggingBeginningSessionConfiguration = _Class(
    "UIDraggingBeginningSessionConfiguration"
)
_UIDruidSourceWarmUpConnection = _Class("_UIDruidSourceWarmUpConnection")
_UIDragManager = _Class("_UIDragManager")
UITableViewUpdateGap = _Class("UITableViewUpdateGap")
_UIPanelAnimationState = _Class("_UIPanelAnimationState")
UIPointerRegion = _Class("UIPointerRegion")
_UICursorRegion = _Class("_UICursorRegion")
UIViewAnimationContext = _Class("UIViewAnimationContext")
UIViewAnimation = _Class("UIViewAnimation")
_UITableViewUpdateSupport = _Class("_UITableViewUpdateSupport")
UIUpdateItem = _Class("UIUpdateItem")
UIDecomposedReloadUpdateItem = _Class("UIDecomposedReloadUpdateItem")
UIRowMoveUpdateItem = _Class("UIRowMoveUpdateItem")
_UITitleContent = _Class("_UITitleContent")
_UISpringLoadedHysteresisBehavior = _Class("_UISpringLoadedHysteresisBehavior")
_UISpringLoadedBlinkingEffect = _Class("_UISpringLoadedBlinkingEffect")
_UIBarButtonSpringLoadedBlinkingEffect = _Class(
    "_UIBarButtonSpringLoadedBlinkingEffect"
)
_UIAppCACommitFuture = _Class("_UIAppCACommitFuture")
_UISheetAnimationController = _Class("_UISheetAnimationController")
UIPanGestureVelocitySample = _Class("UIPanGestureVelocitySample")
UIIndirectScribbleInteraction = _Class("UIIndirectScribbleInteraction")
_UICursorInteraction = _Class("_UICursorInteraction")
_UINavigationParallaxTransition = _Class("_UINavigationParallaxTransition")
UIWebPlugInView = _Class("UIWebPlugInView")
_UICellAccessory = _Class("_UICellAccessory")
_UICellSpacingAccessory = _Class("_UICellSpacingAccessory")
_UICellViewAccessory = _Class("_UICellViewAccessory")
_UIShadowViewImageCacheKey = _Class("_UIShadowViewImageCacheKey")
_UIHyperAsymmetricExtender = _Class("_UIHyperAsymmetricExtender")
_UISheetInteraction = _Class("_UISheetInteraction")
_UISegmentedControlCacheKey = _Class("_UISegmentedControlCacheKey")
_UIScrollViewRefreshControlHost = _Class("_UIScrollViewRefreshControlHost")
_UISelectionGrabberAnimationDelegate = _Class("_UISelectionGrabberAnimationDelegate")
UIDictationMultilingualUtilities = _Class("UIDictationMultilingualUtilities")
_UIMotionEffectEngine = _Class("_UIMotionEffectEngine")
_UITextCursorAssertion = _Class("_UITextCursorAssertion")
_UIUpdateVisibleCellsContext = _Class("_UIUpdateVisibleCellsContext")
UICollectionViewLayoutAttributes = _Class("UICollectionViewLayoutAttributes")
UIDebuggingInformationHierarchyLayoutAttributes = _Class(
    "UIDebuggingInformationHierarchyLayoutAttributes"
)
UITableViewIndexOverlaySelectionViewCollectionViewLayoutAttributes = _Class(
    "UITableViewIndexOverlaySelectionViewCollectionViewLayoutAttributes"
)
UIKeyboardCandidatePocketShadowLayoutAttributes = _Class(
    "UIKeyboardCandidatePocketShadowLayoutAttributes"
)
UICollectionViewTableLayoutAttributes = _Class("UICollectionViewTableLayoutAttributes")
_UICollectionViewListLayoutAttributes = _Class("_UICollectionViewListLayoutAttributes")
_UIFlowLayoutRow = _Class("_UIFlowLayoutRow")
_UIFlowLayoutItem = _Class("_UIFlowLayoutItem")
_UIUndoTextOperation = _Class("_UIUndoTextOperation")
_UITextUndoOperationSetAttributes = _Class("_UITextUndoOperationSetAttributes")
_UITextUndoOperationReplace = _Class("_UITextUndoOperationReplace")
_UITextUndoOperationTyping = _Class("_UITextUndoOperationTyping")
UIRepeatedAction = _Class("UIRepeatedAction")
UIKey = _Class("UIKey")
UIPressInfo = _Class("UIPressInfo")
_UIMenuLeafValidation = _Class("_UIMenuLeafValidation")
UITextRangeAdjustmentInteraction = _Class("UITextRangeAdjustmentInteraction")
UIWindowController = _Class("UIWindowController")
UIKeyboardMediaController = _Class("UIKeyboardMediaController")
_UIStatisticsIntegrator = _Class("_UIStatisticsIntegrator")
UIKBTextEditingTraits = _Class("UIKBTextEditingTraits")
UITextCursorAssertionController = _Class("UITextCursorAssertionController")
_UIFlowLayoutSection = _Class("_UIFlowLayoutSection")
_UIFlowLayoutInfo = _Class("_UIFlowLayoutInfo")
UIKeyboardFloatingTransitionController = _Class(
    "UIKeyboardFloatingTransitionController"
)
UIMorphingLabelGlyphSet = _Class("UIMorphingLabelGlyphSet")
UIDescriptionBuilder = _Class("UIDescriptionBuilder")
_UIFeedbackEngine = _Class("_UIFeedbackEngine")
_UIFeedbackDummyEngine = _Class("_UIFeedbackDummyEngine")
_UIFeedbackSystemSoundEngine = _Class("_UIFeedbackSystemSoundEngine")
_UIFeedbackCoreHapticsEngine = _Class("_UIFeedbackCoreHapticsEngine")
_UIFeedbackCoreHapticsIgnoreCaptureEngine = _Class(
    "_UIFeedbackCoreHapticsIgnoreCaptureEngine"
)
_UIFeedbackCoreHapticsIgnoreCaptureHapticsOnlyEngine = _Class(
    "_UIFeedbackCoreHapticsIgnoreCaptureHapticsOnlyEngine"
)
_UIFeedbackCoreHapticsHapticsOnlyEngine = _Class(
    "_UIFeedbackCoreHapticsHapticsOnlyEngine"
)
_UIFeedbackPreferences = _Class("_UIFeedbackPreferences")
_UIFeedbackParameters = _Class("_UIFeedbackParameters")
_UIFeedbackPatternParameters = _Class("_UIFeedbackPatternParameters")
_UIFeedback = _Class("_UIFeedback")
_UIFeedbackAudioFilePattern = _Class("_UIFeedbackAudioFilePattern")
_UIFeedbackHapticFilePattern = _Class("_UIFeedbackHapticFilePattern")
_UIFeedbackPattern = _Class("_UIFeedbackPattern")
_UIContinuousFeedback = _Class("_UIContinuousFeedback")
_UIDiscreteFeedback = _Class("_UIDiscreteFeedback")
_UICustomDiscreteFeedback = _Class("_UICustomDiscreteFeedback")
_UIRemoteKeyboardsToken = _Class("_UIRemoteKeyboardsToken")
UIKeyboardPredictionCellMetrics = _Class("UIKeyboardPredictionCellMetrics")
UIKeyboardTaskExecutionContext = _Class("UIKeyboardTaskExecutionContext")
UIKeyboardTaskEntry = _Class("UIKeyboardTaskEntry")
_UIScreenEdgePanRecognizer = _Class("_UIScreenEdgePanRecognizer")
UIKeyboardScheduledTask = _Class("UIKeyboardScheduledTask")
UIKBTextStyle = _Class("UIKBTextStyle")
UIKBKeyDisplayContents = _Class("UIKBKeyDisplayContents")
UIKBRenderGeometry = _Class("UIKBRenderGeometry")
UIKeyboardCache = _Class("UIKeyboardCache")
UIKBRenderFactoryLayoutSegment = _Class("UIKBRenderFactoryLayoutSegment")
UIKBEdgeEffect = _Class("UIKBEdgeEffect")
UIKBGradient = _Class("UIKBGradient")
UIKBColorGradient = _Class("UIKBColorGradient")
UIKBRenderTraits = _Class("UIKBRenderTraits")
UIKBRenderingContext = _Class("UIKBRenderingContext")
UIKBCacheToken = _Class("UIKBCacheToken")
UIKBCacheToken_Keyplane = _Class("UIKBCacheToken_Keyplane")
UIKBCacheToken_Key = _Class("UIKBCacheToken_Key")
UIKBCacheToken_KeyFilledTemplate = _Class("UIKBCacheToken_KeyFilledTemplate")
UIKBCacheToken_KeyMask = _Class("UIKBCacheToken_KeyMask")
UIKBCacheToken_KeyTemplate = _Class("UIKBCacheToken_KeyTemplate")
UIKeyboardTransitionSlice = _Class("UIKeyboardTransitionSlice")
UIKBSplitRow = _Class("UIKBSplitRow")
UIKeyboardSliceSet = _Class("UIKeyboardSliceSet")
UIKeyboardSliceStore = _Class("UIKeyboardSliceStore")
UIRivenFactory = _Class("UIRivenFactory")
UIKBSplitKeyplaneGenerator = _Class("UIKBSplitKeyplaneGenerator")
UIKBKeyViewAnimator = _Class("UIKBKeyViewAnimator")
UIKBKeyViewAnimatorMonolith = _Class("UIKBKeyViewAnimatorMonolith")
UIKBKeyViewAnimatorDeveloper = _Class("UIKBKeyViewAnimatorDeveloper")
_UIKeyboardUsageTracking = _Class("_UIKeyboardUsageTracking")
UIKeyboardTypingStyleEstimator = _Class("UIKeyboardTypingStyleEstimator")
_UIKeyboardTypingSpeedLogger = _Class("_UIKeyboardTypingSpeedLogger")
UIKBResizingKeyplaneCoordinator = _Class("UIKBResizingKeyplaneCoordinator")
UIKeyboardHandBiasTransitionCoordinator = _Class(
    "UIKeyboardHandBiasTransitionCoordinator"
)
UIKBGeometry = _Class("UIKBGeometry")
UIKBMergeAction = _Class("UIKBMergeAction")
UIKBTree = _Class("UIKBTree")
UIKBShape = _Class("UIKBShape")
UIKBGraphCache = _Class("UIKBGraphCache")
UIKeyboardCandidateViewConfiguration = _Class("UIKeyboardCandidateViewConfiguration")
UIKeyboardCandidateViewConfigurationTV = _Class(
    "UIKeyboardCandidateViewConfigurationTV"
)
UIKeyboardCandidateViewConfigurationHandwriting = _Class(
    "UIKeyboardCandidateViewConfigurationHandwriting"
)
UIKeyboardCandidateViewConfigurationHandwritingPad = _Class(
    "UIKeyboardCandidateViewConfigurationHandwritingPad"
)
UIKeyboardCandidateViewConfigurationTenKey = _Class(
    "UIKeyboardCandidateViewConfigurationTenKey"
)
UIKeyboardCandidateViewConfigurationTenKeyPadSplit = _Class(
    "UIKeyboardCandidateViewConfigurationTenKeyPadSplit"
)
UIKeyboardCandidateViewConfigurationTenKeyCarPlay = _Class(
    "UIKeyboardCandidateViewConfigurationTenKeyCarPlay"
)
UIKeyboardCandidateViewConfigurationCarPlay = _Class(
    "UIKeyboardCandidateViewConfigurationCarPlay"
)
UIKeyboardCandidateViewConfigurationPhoneInline = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneInline"
)
UIKeyboardCandidateViewConfigurationPhoneVerticalInline = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneVerticalInline"
)
UIKeyboardCandidateViewConfigurationPadVerticalInline = _Class(
    "UIKeyboardCandidateViewConfigurationPadVerticalInline"
)
UIKeyboardCandidateViewConfigurationPadVerticalInlineZhuyin = _Class(
    "UIKeyboardCandidateViewConfigurationPadVerticalInlineZhuyin"
)
UIKeyboardCandidateViewConfigurationPadInline = _Class(
    "UIKeyboardCandidateViewConfigurationPadInline"
)
UIKeyboardCandidateViewConfigurationPadInlineLiveConversion = _Class(
    "UIKeyboardCandidateViewConfigurationPadInlineLiveConversion"
)
UIKeyboardCandidateViewConfigurationPadInlineLiveConversionZhuyin = _Class(
    "UIKeyboardCandidateViewConfigurationPadInlineLiveConversionZhuyin"
)
UIKeyboardCandidateViewConfigurationPhoneBar = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBar"
)
UIKeyboardCandidateViewConfigurationPhoneBarLandscape = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarLandscape"
)
UIKeyboardCandidateViewConfigurationPhoneBarLandscapeWithBottomPadding = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarLandscapeWithBottomPadding"
)
UIKeyboardCandidateViewConfigurationPhoneBarTall = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarTall"
)
UIKeyboardCandidateViewConfigurationPhoneBarWithBottomPadding = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarWithBottomPadding"
)
UIKeyboardCandidateViewConfigurationPadBar = _Class(
    "UIKeyboardCandidateViewConfigurationPadBar"
)
UIKeyboardCandidateViewConfigurationPadSplitBar = _Class(
    "UIKeyboardCandidateViewConfigurationPadSplitBar"
)
UIKeyboardCandidateViewConfigurationPadSplitBarJapanese = _Class(
    "UIKeyboardCandidateViewConfigurationPadSplitBarJapanese"
)
UIKeyboardCandidateViewConfigurationPadBarLandscape = _Class(
    "UIKeyboardCandidateViewConfigurationPadBarLandscape"
)
UIKeyboardCandidateViewConfigurationPhoneBarDown = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarDown"
)
UIKeyboardCandidateViewConfigurationPadFloatingBar = _Class(
    "UIKeyboardCandidateViewConfigurationPadFloatingBar"
)
UIKeyboardCandidateViewConfigurationPhoneBarDownWithBottomPadding = _Class(
    "UIKeyboardCandidateViewConfigurationPhoneBarDownWithBottomPadding"
)
UIKBKeyplaneChangeContext = _Class("UIKBKeyplaneChangeContext")
_UIResponder_Override_Host_Entry = _Class("_UIResponder_Override_Host_Entry")
_UIResponder_Override_Host = _Class("_UIResponder_Override_Host")
_UIResponder_Override = _Class("_UIResponder_Override")
_UIFieldEditorHost = _Class("_UIFieldEditorHost")
_UIFieldEditorSystemInputHost = _Class("_UIFieldEditorSystemInputHost")
_UIFieldEditorPasscodeHost = _Class("_UIFieldEditorPasscodeHost")
_UITouchForwardingRecipient = _Class("_UITouchForwardingRecipient")
UILongPressGestureVelocitySample = _Class("UILongPressGestureVelocitySample")
UIGestureDelayedTouch = _Class("UIGestureDelayedTouch")
_UISEGestureFeature = _Class("_UISEGestureFeature")
_UISEIdleTimerFailGestureFeature = _Class("_UISEIdleTimerFailGestureFeature")
_UISEHybridEdgesFailGestureFeature = _Class("_UISEHybridEdgesFailGestureFeature")
_UISEFirmwareEdgesFailGestureFeature = _Class("_UISEFirmwareEdgesFailGestureFeature")
_UISEEdgeTypeForceRecognizeGestureFeature = _Class(
    "_UISEEdgeTypeForceRecognizeGestureFeature"
)
_UISEDiagonalHysteresisRecognizeGestureFeature = _Class(
    "_UISEDiagonalHysteresisRecognizeGestureFeature"
)
_UISEPerTypeEdgesFailGestureFeature = _Class("_UISEPerTypeEdgesFailGestureFeature")
_UISEAnyGestureFeature = _Class("_UISEAnyGestureFeature")
_UISEAllGestureFeature = _Class("_UISEAllGestureFeature")
_UISEEdgeTypeRecognizeGestureFeature = _Class("_UISEEdgeTypeRecognizeGestureFeature")
_UISEVelocityDirectionEdgesGestureFeature = _Class(
    "_UISEVelocityDirectionEdgesGestureFeature"
)
_UISEOrthogonalHysteresisGestureFeature = _Class(
    "_UISEOrthogonalHysteresisGestureFeature"
)
_UISEBackProjectEdgesFailGestureFeature = _Class(
    "_UISEBackProjectEdgesFailGestureFeature"
)
_UISETeleportFailGestureFeature = _Class("_UISETeleportFailGestureFeature")
_UISEEdgeTypeFailGestureFeature = _Class("_UISEEdgeTypeFailGestureFeature")
_UISEInitialEdgesFailGestureFeature = _Class("_UISEInitialEdgesFailGestureFeature")
_UISEMuxGestureFeature = _Class("_UISEMuxGestureFeature")
_UIWeakDisplayLinkTarget = _Class("_UIWeakDisplayLinkTarget")
UIDelayedAction = _Class("UIDelayedAction")
UIHeldAction = _Class("UIHeldAction")
_UIAnalyticsTouchesSession = _Class("_UIAnalyticsTouchesSession")
_UIRKEOTouchTracking = _Class("_UIRKEOTouchTracking")
_UIDragSessionImpl = _Class("_UIDragSessionImpl")
UIAnimation = _Class("UIAnimation")
UIScrollAnimation = _Class("UIScrollAnimation")
UIFrameAnimation = _Class("UIFrameAnimation")
UIScrollViewScrollAnimation = _Class("UIScrollViewScrollAnimation")
UIAnimator = _Class("UIAnimator")
UITouchData = _Class("UITouchData")
UIKeyCommandDiscoverabilityHUD = _Class("UIKeyCommandDiscoverabilityHUD")
_UIHIDContext = _Class("_UIHIDContext")
_UIPencilPreferences = _Class("_UIPencilPreferences")
UICommandAlternate = _Class("UICommandAlternate")
UIKeyboardMotionSupport = _Class("UIKeyboardMotionSupport")
UIScrollToDismissSupport = _Class("UIScrollToDismissSupport")
UISplitKeyboardSupport = _Class("UISplitKeyboardSupport")
_UIInputViewKeyboardOutput = _Class("_UIInputViewKeyboardOutput")
TIKeyboardCandidateSuggestion = _Class("TIKeyboardCandidateSuggestion")
UITextReplacementCandidate = _Class("UITextReplacementCandidate")
UIInputViewControllerInterface = _Class("UIInputViewControllerInterface")
_UITextDocumentInterface = _Class("_UITextDocumentInterface")
UIKBAutofillController = _Class("UIKBAutofillController")
UIKeyboardCandidateController = _Class("UIKeyboardCandidateController")
UIKeyboardAutocorrectionController = _Class("UIKeyboardAutocorrectionController")
_UIKeyboardImplProxy = _Class("_UIKeyboardImplProxy")
UIKeyboardTaskQueue = _Class("UIKeyboardTaskQueue")
_UIButtonBarTargetAction = _Class("_UIButtonBarTargetAction")
_UISceneDisplayLinkTargetAndAction = _Class("_UISceneDisplayLinkTargetAndAction")
_UISceneDisplayLink = _Class("_UISceneDisplayLink")
UICellAccessoryConfiguration = _Class("UICellAccessoryConfiguration")
_UIBackgroundViewConfiguration = _Class("_UIBackgroundViewConfiguration")
UIBackgroundConfiguration = _Class("UIBackgroundConfiguration")
UITableCellAccessoryLayout = _Class("UITableCellAccessoryLayout")
UICellAccessoryManager = _Class("UICellAccessoryManager")
UITableViewCellLayoutManager = _Class("UITableViewCellLayoutManager")
UITableViewCellLayoutManagerValue2 = _Class("UITableViewCellLayoutManagerValue2")
UITableViewCellLayoutManagerValue1 = _Class("UITableViewCellLayoutManagerValue1")
UITableViewCellLayoutManagerEditable1 = _Class("UITableViewCellLayoutManagerEditable1")
UIMoreListCellLayoutManager = _Class("UIMoreListCellLayoutManager")
UITableViewCellLayoutManagerSubtitle = _Class("UITableViewCellLayoutManagerSubtitle")
UIViewConfigurationState = _Class("UIViewConfigurationState")
UICellConfigurationState = _Class("UICellConfigurationState")
_UIContentViewLabelConfiguration = _Class("_UIContentViewLabelConfiguration")
_UIContentViewImageViewConfiguration = _Class("_UIContentViewImageViewConfiguration")
_UIBasicCellContentViewConfiguration = _Class("_UIBasicCellContentViewConfiguration")
_UITableViewReorderingSupport = _Class("_UITableViewReorderingSupport")
_UIButtonBarLayout = _Class("_UIButtonBarLayout")
_UIButtonBarSpacerLayout = _Class("_UIButtonBarSpacerLayout")
_UIButtonBarItemLayout = _Class("_UIButtonBarItemLayout")
_UIButtonBarItemGroupLayout = _Class("_UIButtonBarItemGroupLayout")
UINavigationContentAdjustments = _Class("UINavigationContentAdjustments")
UISectionRowData = _Class("UISectionRowData")
UITableViewRowData = _Class("UITableViewRowData")
UINavigationDeferredTransitionContext = _Class("UINavigationDeferredTransitionContext")
_UIBarButtonItemDataBaseFallback = _Class("_UIBarButtonItemDataBaseFallback")
_UIBarAppearanceData = _Class("_UIBarAppearanceData")
_UINavTitleAppearanceData = _Class("_UINavTitleAppearanceData")
_UITabBarItemData = _Class("_UITabBarItemData")
_UITabBarLayoutData = _Class("_UITabBarLayoutData")
_UIBarBackgroundAppearanceData = _Class("_UIBarBackgroundAppearanceData")
_UIBarButtonItemData = _Class("_UIBarButtonItemData")
_UINavigationBarVisualStyle = _Class("_UINavigationBarVisualStyle")
_UINavigationBarTVVisualStyle = _Class("_UINavigationBarTVVisualStyle")
_UINavigationBarStarkVisualStyle = _Class("_UINavigationBarStarkVisualStyle")
_UINavigationBarPhonePadVisualStyle = _Class("_UINavigationBarPhonePadVisualStyle")
_UIBarAppearanceStorage = _Class("_UIBarAppearanceStorage")
_UIToolbarAppearanceStorage = _Class("_UIToolbarAppearanceStorage")
_UINavigationBarAppearanceStorage = _Class("_UINavigationBarAppearanceStorage")
_UIBarInsertLayoutData = _Class("_UIBarInsertLayoutData")
_UINavigationBarLayout = _Class("_UINavigationBarLayout")
UISlidingBarStateRequest = _Class("UISlidingBarStateRequest")
UISlidingBarState = _Class("UISlidingBarState")
_UIAppearanceRecorder = _Class("_UIAppearanceRecorder")
_UITableViewDropController = _Class("_UITableViewDropController")
_UITableViewDragController = _Class("_UITableViewDragController")
_UISwipeHandler = _Class("_UISwipeHandler")
UISwipeActionController = _Class("UISwipeActionController")
_UITableViewSubviewManager = _Class("_UITableViewSubviewManager")
UITableConstants_IOS = _Class("UITableConstants_IOS")
UITableConstants_Phone = _Class("UITableConstants_Phone")
UITableConstants_Watch = _Class("UITableConstants_Watch")
UITableConstants_Pad = _Class("UITableConstants_Pad")
UIPopoverController = _Class("UIPopoverController")
_UIViewServiceDummyPopoverController = _Class("_UIViewServiceDummyPopoverController")
UIDeviceAppearanceContainer = _Class("UIDeviceAppearanceContainer")
UITestOneAppearanceContainer = _Class("UITestOneAppearanceContainer")
UITestTwoAppearanceContainer = _Class("UITestTwoAppearanceContainer")
UIPhoneAppearanceContainer = _Class("UIPhoneAppearanceContainer")
UIPadAppearanceContainer = _Class("UIPadAppearanceContainer")
_UITextInputStringTokenizerSubrange = _Class("_UITextInputStringTokenizerSubrange")
_UIViewAdditiveAnimationAction = _Class("_UIViewAdditiveAnimationAction")
_UIAssistantEntry = _Class("_UIAssistantEntry")
_UIButtonBarLayoutMetrics = _Class("_UIButtonBarLayoutMetrics")
_UIButtonBar = _Class("_UIButtonBar")
UITextInputPasswordRules = _Class("UITextInputPasswordRules")
_UIAccessibilityLimits = _Class("_UIAccessibilityLimits")
_UIToolbarVisualProvider = _Class("_UIToolbarVisualProvider")
_UIToolbarVisualProviderLegacyIOS = _Class("_UIToolbarVisualProviderLegacyIOS")
_UIToolbarVisualProviderModernIOS = _Class("_UIToolbarVisualProviderModernIOS")
_UIKeyboardTextSelectionController = _Class("_UIKeyboardTextSelectionController")
_UIKeyboardAsyncTextSelectionController = _Class(
    "_UIKeyboardAsyncTextSelectionController"
)
_UIViewFittingSizeTargetInfo = _Class("_UIViewFittingSizeTargetInfo")
_UIWeakHelper = _Class("_UIWeakHelper")
UIMultiSelectInteraction = _Class("UIMultiSelectInteraction")
_UICollectionViewMultiSelectController = _Class(
    "_UICollectionViewMultiSelectController"
)
_UICollectionViewOrthogonalScrollerSectionController = _Class(
    "_UICollectionViewOrthogonalScrollerSectionController"
)
_UICollectionViewShadowUpdatesController = _Class(
    "_UICollectionViewShadowUpdatesController"
)
_UICollectionViewDragAndDropController = _Class(
    "_UICollectionViewDragAndDropController"
)
UICollectionViewData = _Class("UICollectionViewData")
_UICollectionViewSelectionController = _Class("_UICollectionViewSelectionController")
UICollectionViewLayoutInvalidationContext = _Class(
    "UICollectionViewLayoutInvalidationContext"
)
_UICollectionViewCompositionLayoutInvalidationContext = _Class(
    "_UICollectionViewCompositionLayoutInvalidationContext"
)
UICollectionViewTableLayoutInvalidationContext = _Class(
    "UICollectionViewTableLayoutInvalidationContext"
)
_UICollectionViewListLayoutInvalidationContext = _Class(
    "_UICollectionViewListLayoutInvalidationContext"
)
UICollectionViewFlowLayoutInvalidationContext = _Class(
    "UICollectionViewFlowLayoutInvalidationContext"
)
EmojiSectionHeaderLayoutInvalidationContext = _Class(
    "EmojiSectionHeaderLayoutInvalidationContext"
)
UICollectionViewLayout = _Class("UICollectionViewLayout")
UIDebuggingInformationHierarchyLayout = _Class("UIDebuggingInformationHierarchyLayout")
_UICollectionViewListLayout = _Class("_UICollectionViewListLayout")
_UICollectionViewCompositionLayout = _Class("_UICollectionViewCompositionLayout")
UICollectionViewTableLayout = _Class("UICollectionViewTableLayout")
UICollectionViewCompositionalLayout = _Class("UICollectionViewCompositionalLayout")
_UICollectionViewCompositionalLayout = _Class("_UICollectionViewCompositionalLayout")
UICollectionViewTransitionLayout = _Class("UICollectionViewTransitionLayout")
UICollectionViewFlowLayout = _Class("UICollectionViewFlowLayout")
UITableViewIndexOverlaySelectionViewCollectionViewFlowLayout = _Class(
    "UITableViewIndexOverlaySelectionViewCollectionViewFlowLayout"
)
UIKeyboardEmojiLayout = _Class("UIKeyboardEmojiLayout")
_UILAConfigurationHistory = _Class("_UILAConfigurationHistory")
_UIOLAConfigurationHistory = _Class("_UIOLAConfigurationHistory")
_UIALAConfigurationHistory = _Class("_UIALAConfigurationHistory")
_UILayoutArrangement = _Class("_UILayoutArrangement")
_UIAlignedLayoutArrangement = _Class("_UIAlignedLayoutArrangement")
_UIOrderedLayoutArrangement = _Class("_UIOrderedLayoutArrangement")
UITextPasteController = _Class("UITextPasteController")
UITextLoupeCursorBehavior = _Class("UITextLoupeCursorBehavior")
UITextMagnifierTimeWeightedPoint = _Class("UITextMagnifierTimeWeightedPoint")
_UIKeyboardTextSelectionGestureController = _Class(
    "_UIKeyboardTextSelectionGestureController"
)
_UIKeyboardBasedTextSelectionGestureController = _Class(
    "_UIKeyboardBasedTextSelectionGestureController"
)
_UIKeyboardBasedNonEditableTextSelectionGestureController = _Class(
    "_UIKeyboardBasedNonEditableTextSelectionGestureController"
)
UITextLoupeTouchBehavior = _Class("UITextLoupeTouchBehavior")
_UILongPressClickInteractionDriver = _Class("_UILongPressClickInteractionDriver")
_UICoversheetClickInteractionDriver = _Class("_UICoversheetClickInteractionDriver")
_UILongPressTimeoutClickInteractionDriver = _Class(
    "_UILongPressTimeoutClickInteractionDriver"
)
_UIControlCenterClickInteractionDriver = _Class(
    "_UIControlCenterClickInteractionDriver"
)
_UIControlLongPressClickInteractionDriver = _Class(
    "_UIControlLongPressClickInteractionDriver"
)
_UISecondaryClickClickInteractionDriver = _Class(
    "_UISecondaryClickClickInteractionDriver"
)
_UIClickPresentationInteraction = _Class("_UIClickPresentationInteraction")
UITextSelection = _Class("UITextSelection")
UITextInteractionAssistant = _Class("UITextInteractionAssistant")
UIWKTextInteractionAssistant = _Class("UIWKTextInteractionAssistant")
_UIDragInteractionDriver = _Class("_UIDragInteractionDriver")
_UIDragInteractionClickPresentationDriver = _Class(
    "_UIDragInteractionClickPresentationDriver"
)
_UIDragInteractionLongPressDriver = _Class("_UIDragInteractionLongPressDriver")
_UIDragSourceLiftEffect = _Class("_UIDragSourceLiftEffect")
UITextDragAssistant = _Class("UITextDragAssistant")
UITextDragDropSupport = _Class("UITextDragDropSupport")
UILayoutManagerBasedDraggableGeometry = _Class("UILayoutManagerBasedDraggableGeometry")
_UITextViewContentPadding = _Class("_UITextViewContentPadding")
_UITextViewVisualStyle = _Class("_UITextViewVisualStyle")
_UITextViewVisualStyle_tvOS = _Class("_UITextViewVisualStyle_tvOS")
_UITextViewVisualStyle_iOS = _Class("_UITextViewVisualStyle_iOS")
_UITextViewRestorableScrollPosition = _Class("_UITextViewRestorableScrollPosition")
UITextInteraction = _Class("UITextInteraction")
UITextPhraseBoundaryInteraction = _Class("UITextPhraseBoundaryInteraction")
UITextLiveConversionInteraction = _Class("UITextLiveConversionInteraction")
_UITextContextMenuInteractionBase = _Class("_UITextContextMenuInteractionBase")
_UIContextMenuInteractionBasedTextContextInteraction = _Class(
    "_UIContextMenuInteractionBasedTextContextInteraction"
)
_UIMenuControllerBasedTextContextInteraction = _Class(
    "_UIMenuControllerBasedTextContextInteraction"
)
UITextServicesInteraction = _Class("UITextServicesInteraction")
UITextContextMenuInteraction = _Class("UITextContextMenuInteraction")
UITextNonEditableInteraction = _Class("UITextNonEditableInteraction")
UITextIndirectEditableInteraction = _Class("UITextIndirectEditableInteraction")
UITextIndirectNonEditableInteraction = _Class("UITextIndirectNonEditableInteraction")
_UIKeyboardTextSelectionInteraction = _Class("_UIKeyboardTextSelectionInteraction")
_UIKeyboardBasedTextSelectionInteraction = _Class(
    "_UIKeyboardBasedTextSelectionInteraction"
)
_UIKeyboardBasedNonEditableTextSelectionInteraction = _Class(
    "_UIKeyboardBasedNonEditableTextSelectionInteraction"
)
UITextIndirectKeyboardInteraction = _Class("UITextIndirectKeyboardInteraction")
UITextSelectionInteraction = _Class("UITextSelectionInteraction")
UIWKTextSelectionInteraction = _Class("UIWKTextSelectionInteraction")
UITextLoupeInteraction = _Class("UITextLoupeInteraction")
UITextLoupeInteraction_CustomHighlighter = _Class(
    "UITextLoupeInteraction_CustomHighlighter"
)
UITextItemInteractionInteraction = _Class("UITextItemInteractionInteraction")
_UITextSimpleLinkInteraction = _Class("_UITextSimpleLinkInteraction")
_UITextLongPressLinkInteraction = _Class("_UITextLongPressLinkInteraction")
_UITextMenuLinkInteraction = _Class("_UITextMenuLinkInteraction")
UITextLinkInteraction = _Class("UITextLinkInteraction")
UISearchToken = _Class("UISearchToken")
_UISearchToken = _Class("_UISearchToken")
UIScreenshotService = _Class("UIScreenshotService")
UIContextMenuInteraction = _Class("UIContextMenuInteraction")
_UIVariableGestureContextMenuInteraction = _Class(
    "_UIVariableGestureContextMenuInteraction"
)
UIBarButtonItemStateAppearance = _Class("UIBarButtonItemStateAppearance")
UIBarButtonItemAppearance = _Class("UIBarButtonItemAppearance")
UITabBarItemStateAppearance = _Class("UITabBarItemStateAppearance")
UITabBarItemAppearance = _Class("UITabBarItemAppearance")
UIBarAppearance = _Class("UIBarAppearance")
UITabBarAppearance = _Class("UITabBarAppearance")
UIToolbarAppearance = _Class("UIToolbarAppearance")
UINavigationBarAppearance = _Class("UINavigationBarAppearance")
UIFontPickerViewControllerConfiguration = _Class(
    "UIFontPickerViewControllerConfiguration"
)
UIDictationPhrase = _Class("UIDictationPhrase")
UITextInputStringTokenizer = _Class("UITextInputStringTokenizer")
_UITextInputControllerTokenizer = _Class("_UITextInputControllerTokenizer")
_UITextPlaceholderAttachment = _Class("_UITextPlaceholderAttachment")
_UIImageTextAttachment = _Class("_UIImageTextAttachment")
_UISearchTokenAttachment = _Class("_UISearchTokenAttachment")
UITextSelectionRect = _Class("UITextSelectionRect")
_UITextSelectionCaretRect = _Class("_UITextSelectionCaretRect")
UISimpleSelectionRect = _Class("UISimpleSelectionRect")
UITextSelectionRectImpl = _Class("UITextSelectionRectImpl")
_UITextKitSelectionRect = _Class("_UITextKitSelectionRect")
UITextChecker = _Class("UITextChecker")
UIFontMetrics = _Class("UIFontMetrics")
UIPrintFormatter = _Class("UIPrintFormatter")
UITallPDFPrintFormatter = _Class("UITallPDFPrintFormatter")
UIMarkupTextPrintFormatter = _Class("UIMarkupTextPrintFormatter")
UISimpleTextPrintFormatter = _Class("UISimpleTextPrintFormatter")
UIViewPrintFormatter = _Class("UIViewPrintFormatter")
UIWebDocumentViewPrintFormatter = _Class("UIWebDocumentViewPrintFormatter")
UIWebViewPrintFormatter = _Class("UIWebViewPrintFormatter")
UITextViewPrintFormatter = _Class("UITextViewPrintFormatter")
UIPrintPaper = _Class("UIPrintPaper")
UIPrintInfo = _Class("UIPrintInfo")
UIPrinter = _Class("UIPrinter")
UIPrintPageRenderer = _Class("UIPrintPageRenderer")
UIPrintInteractionController = _Class("UIPrintInteractionController")
UIAccessibilityLocationDescriptor = _Class("UIAccessibilityLocationDescriptor")
UIAccessibilityCustomRotorSearchPredicate = _Class(
    "UIAccessibilityCustomRotorSearchPredicate"
)
UIAccessibilityCustomRotorItemResult = _Class("UIAccessibilityCustomRotorItemResult")
UIAccessibilityCustomRotor = _Class("UIAccessibilityCustomRotor")
UIAccessibilityCustomAction = _Class("UIAccessibilityCustomAction")
UIApplicationShortcutItem = _Class("UIApplicationShortcutItem")
UIMutableApplicationShortcutItem = _Class("UIMutableApplicationShortcutItem")
UIApplicationShortcutIcon = _Class("UIApplicationShortcutIcon")
UIPreviewInteraction = _Class("UIPreviewInteraction")
UIPreviewActionGroup = _Class("UIPreviewActionGroup")
UIPreviewAction = _Class("UIPreviewAction")
UIFocusAnimationCoordinator = _Class("UIFocusAnimationCoordinator")
UIFocusDebugger = _Class("UIFocusDebugger")
UIFocusMovementHint = _Class("UIFocusMovementHint")
UIFocusUpdateContext = _Class("UIFocusUpdateContext")
UITableViewFocusUpdateContext = _Class("UITableViewFocusUpdateContext")
UICollectionViewFocusUpdateContext = _Class("UICollectionViewFocusUpdateContext")
UIPencilInteraction = _Class("UIPencilInteraction")
UITargetedPreview = _Class("UITargetedPreview")
_UITargetedPreview = _Class("_UITargetedPreview")
UITargetedDragPreview = _Class("UITargetedDragPreview")
UIPreviewTarget = _Class("UIPreviewTarget")
_UIPreviewTarget = _Class("_UIPreviewTarget")
UIDragPreviewTarget = _Class("UIDragPreviewTarget")
UIDragPreview = _Class("UIDragPreview")
UIPreviewParameters = _Class("UIPreviewParameters")
_UIPreviewParameters = _Class("_UIPreviewParameters")
UIDragPreviewParameters = _Class("UIDragPreviewParameters")
UIDropProposal = _Class("UIDropProposal")
UITextDropProposal = _Class("UITextDropProposal")
UITableViewDropProposal = _Class("UITableViewDropProposal")
UICollectionViewDropProposal = _Class("UICollectionViewDropProposal")
UIDragItem = _Class("UIDragItem")
_UIDropItem = _Class("_UIDropItem")
UIDropInteraction = _Class("UIDropInteraction")
UIDragInteraction = _Class("UIDragInteraction")
UIPress = _Class("UIPress")
UITouch = _Class("UITouch")
UIScreenMode = _Class("UIScreenMode")
UIAlertAction = _Class("UIAlertAction")
UIPrinterPickerController = _Class("UIPrinterPickerController")
UILexiconEntry = _Class("UILexiconEntry")
UILexicon = _Class("UILexicon")
UIStoryboardUnwindSegueSource = _Class("UIStoryboardUnwindSegueSource")
UIStoryboardSegue = _Class("UIStoryboardSegue")
UIStoryboardPopoverSegue = _Class("UIStoryboardPopoverSegue")
UIPasteConfiguration = _Class("UIPasteConfiguration")
NSDocumentDifferenceSize = _Class("NSDocumentDifferenceSize")
_UIDocumentPickerNSURLWrapper = _Class("_UIDocumentPickerNSURLWrapper")
UIDocument = _Class("UIDocument")
UIManagedDocument = _Class("UIManagedDocument")
_UIViewControllerNullAnimationTransitionCoordinator = _Class(
    "_UIViewControllerNullAnimationTransitionCoordinator"
)
_UISplitViewControllerColumnContents = _Class("_UISplitViewControllerColumnContents")
_UITouchForceObservable = _Class("_UITouchForceObservable")
UIForceStageObservable = _Class("UIForceStageObservable")
_UIHyperConstantExtender = _Class("_UIHyperConstantExtender")
_UIHyperspace = _Class("_UIHyperspace")
_UIHyperInteractor = _Class("_UIHyperInteractor")
_UIHyperrectangle = _Class("_UIHyperrectangle")
_UIHyperregionUnion = _Class("_UIHyperregionUnion")
_UIHyperpoint = _Class("_UIHyperpoint")
UISlidingBarConfiguration = _Class("UISlidingBarConfiguration")
_UIPanelInternalState = _Class("_UIPanelInternalState")
UIPanelController = _Class("UIPanelController")
UISplitViewControllerPanelImpl = _Class("UISplitViewControllerPanelImpl")
_UIBarBackgroundLayout = _Class("_UIBarBackgroundLayout")
_UIBarBackgroundLayoutModern = _Class("_UIBarBackgroundLayoutModern")
_UIBarBackgroundLayoutLegacy = _Class("_UIBarBackgroundLayoutLegacy")
_UINavigationBarItemStackEntry = _Class("_UINavigationBarItemStackEntry")
_UISEGestureFeatureSettings = _Class("_UISEGestureFeatureSettings")
UIPercentDrivenInteractiveTransition = _Class("UIPercentDrivenInteractiveTransition")
_UIPreviewTransitionController = _Class("_UIPreviewTransitionController")
_UIAlertControllerInteractionController = _Class(
    "_UIAlertControllerInteractionController"
)
_UINavigationInteractiveTransitionBase = _Class(
    "_UINavigationInteractiveTransitionBase"
)
_UINavigationInteractiveTransition = _Class("_UINavigationInteractiveTransition")
_UINavigationControllerRefreshControlHost = _Class(
    "_UINavigationControllerRefreshControlHost"
)
_UINavigationBarLargeTitleViewLayout = _Class("_UINavigationBarLargeTitleViewLayout")
_UINavigationBarContentViewLayout = _Class("_UINavigationBarContentViewLayout")
_UINavigationBarItemStack = _Class("_UINavigationBarItemStack")
_UINavigationBarVisualProvider = _Class("_UINavigationBarVisualProvider")
_UINavigationBarVisualProviderModernCarPlay = _Class(
    "_UINavigationBarVisualProviderModernCarPlay"
)
_UINavigationBarVisualProviderLegacyIOS = _Class(
    "_UINavigationBarVisualProviderLegacyIOS"
)
_UINavigationBarVisualProviderModernIOS = _Class(
    "_UINavigationBarVisualProviderModernIOS"
)
_UIAppearanceCustomizableClassInfo = _Class("_UIAppearanceCustomizableClassInfo")
_UICompoundObjectMap = _Class("_UICompoundObjectMap")
_UIViewControllerKeyboardAnimationStyleInfo = _Class(
    "_UIViewControllerKeyboardAnimationStyleInfo"
)
UIInputViewAnimationControllerBasic = _Class("UIInputViewAnimationControllerBasic")
UIInputViewPlacementTransition = _Class("UIInputViewPlacementTransition")
UIInputViewSetNotificationInfo = _Class("UIInputViewSetNotificationInfo")
UIKBAnalyticsDispatcher = _Class("UIKBAnalyticsDispatcher")
UIViewControllerAction = _Class("UIViewControllerAction")
_UIStatistics = _Class("_UIStatistics")
_UIStatisticsDistribution = _Class("_UIStatisticsDistribution")
_UIStatisticsScalar = _Class("_UIStatisticsScalar")
_UIScreenBoundingPathUtilities = _Class("_UIScreenBoundingPathUtilities")
_UIScreenRectangularBoundingPathUtilities = _Class(
    "_UIScreenRectangularBoundingPathUtilities"
)
_UIScreenComplexBoundingPathUtilities = _Class("_UIScreenComplexBoundingPathUtilities")
_UIFenceTask = _Class("_UIFenceTask")
_UISceneScreenBasedMetricsCalculator = _Class("_UISceneScreenBasedMetricsCalculator")
_UISceneUnassociatedContext = _Class("_UISceneUnassociatedContext")
_UIViewServiceReplyControlProxy = _Class("_UIViewServiceReplyControlProxy")
_UITextServiceSession = _Class("_UITextServiceSession")
_UIHostedTextServiceSession = _Class("_UIHostedTextServiceSession")
_UIAsyncInvocationObserver = _Class("_UIAsyncInvocationObserver")
UIKeyboardBIUImageGenerator = _Class("UIKeyboardBIUImageGenerator")
UIBarButtonItemGroup = _Class("UIBarButtonItemGroup")
_UIViewServiceDeputyXPCInterfaceInvocationFactory = _Class(
    "_UIViewServiceDeputyXPCInterfaceInvocationFactory"
)
_UIRemoteViewControllerWeakWrapperProxy = _Class(
    "_UIRemoteViewControllerWeakWrapperProxy"
)
_UIHostedWindowHostingHandle = _Class("_UIHostedWindowHostingHandle")
_UIBoundingPath = _Class("_UIBoundingPath")
_UIComplexBoundingPath = _Class("_UIComplexBoundingPath")
_UIRectangularBoundingPath = _Class("_UIRectangularBoundingPath")
_UIViewControllerTransitionCoordinatorContextDescription = _Class(
    "_UIViewControllerTransitionCoordinatorContextDescription"
)
_UIViewServiceControllerOperatorCreateResult = _Class(
    "_UIViewServiceControllerOperatorCreateResult"
)
_UIViewServiceViewControllerOperatorCreateOptions = _Class(
    "_UIViewServiceViewControllerOperatorCreateOptions"
)
_UIViewAnimationAttributes = _Class("_UIViewAnimationAttributes")
UISpringTimingParameters = _Class("UISpringTimingParameters")
_UITextServiceSessionContext = _Class("_UITextServiceSessionContext")
_UIViewServiceDeputyManager = _Class("_UIViewServiceDeputyManager")
_UIViewServiceInterfaceConnectionRequest = _Class(
    "_UIViewServiceInterfaceConnectionRequest"
)
_UIViewServiceInterface = _Class("_UIViewServiceInterface")
_UIViewControllerControlMessageDeputyXPCInterface = _Class(
    "_UIViewControllerControlMessageDeputyXPCInterface"
)
_UIViewServiceTextEffectsOperator_XPCInterface = _Class(
    "_UIViewServiceTextEffectsOperator_XPCInterface"
)
_UIViewServiceTextEffectsOperator = _Class("_UIViewServiceTextEffectsOperator")
_UIViewServiceViewControllerOperator_XPCInterface = _Class(
    "_UIViewServiceViewControllerOperator_XPCInterface"
)
UITextInputAssistantItem = _Class("UITextInputAssistantItem")
UISystemDefaultTextInputAssistantItem = _Class("UISystemDefaultTextInputAssistantItem")
UIAssistantBarButtonItemProvider = _Class("UIAssistantBarButtonItemProvider")
_UIActionWhenIdle = _Class("_UIActionWhenIdle")
_UIGestureRecognizerTransformAnalyzer = _Class("_UIGestureRecognizerTransformAnalyzer")
UIUndoGestureInteraction = _Class("UIUndoGestureInteraction")
UIPeripheralHost = _Class("UIPeripheralHost")
_UIAsyncInvocation = _Class("_UIAsyncInvocation")
_UIRemoteViewControllerConnectionInfo = _Class("_UIRemoteViewControllerConnectionInfo")
_UIRemoteViewControllerConnectionRequest = _Class(
    "_UIRemoteViewControllerConnectionRequest"
)
_UIViewServiceViewControllerDeputyXPCInterface = _Class(
    "_UIViewServiceViewControllerDeputyXPCInterface"
)
_UIRemoteViewService = _Class("_UIRemoteViewService")
_UIKeyboardChangedInformation = _Class("_UIKeyboardChangedInformation")
_UIKeyboardChangedInformationWithFencing = _Class(
    "_UIKeyboardChangedInformationWithFencing"
)
_UITextSizeCache = _Class("_UITextSizeCache")
UIItemProvider = _Class("UIItemProvider")
WebThreadSafeUndoManager = _Class("WebThreadSafeUndoManager")
_UITextUndoManager = _Class("_UITextUndoManager")
UIInputViewSetPlacement_GenericApplicator = _Class(
    "UIInputViewSetPlacement_GenericApplicator"
)
UIInputViewSetPlacement_UndockedApplicator = _Class(
    "UIInputViewSetPlacement_UndockedApplicator"
)
UIInputViewSetPlacement_FloatingApplicator = _Class(
    "UIInputViewSetPlacement_FloatingApplicator"
)
UIInputViewSetPlacement_DockResponderApplicator = _Class(
    "UIInputViewSetPlacement_DockResponderApplicator"
)
UIInputViewSetPlacement_DragToDismissApplicator = _Class(
    "UIInputViewSetPlacement_DragToDismissApplicator"
)
UIInputViewSetPlacement_AssistantApplicator = _Class(
    "UIInputViewSetPlacement_AssistantApplicator"
)
UIKBRenderFactory = _Class("UIKBRenderFactory")
UIKBRenderFactory_Monolith = _Class("UIKBRenderFactory_Monolith")
UIKBRenderFactory_MonolithLinear = _Class("UIKBRenderFactory_MonolithLinear")
UIKBRenderFactory_MonolithLinearSlim = _Class("UIKBRenderFactory_MonolithLinearSlim")
UIKBRenderFactory_Emoji = _Class("UIKBRenderFactory_Emoji")
UIKBRenderFactoryEmoji_iPad_Split = _Class("UIKBRenderFactoryEmoji_iPad_Split")
UIKBRenderFactoryEmoji_iPhone = _Class("UIKBRenderFactoryEmoji_iPhone")
UIKBRenderFactoryEmoji_iPad = _Class("UIKBRenderFactoryEmoji_iPad")
UIKBRenderFactoryEmoji_iPad_Landscape = _Class("UIKBRenderFactoryEmoji_iPad_Landscape")
UIKBRenderFactory_Car = _Class("UIKBRenderFactory_Car")
UIKBRenderFactory_CarLinear = _Class("UIKBRenderFactory_CarLinear")
UIKBRenderFactory_CarTenKey = _Class("UIKBRenderFactory_CarTenKey")
UIKBRenderFactory_Candidates = _Class("UIKBRenderFactory_Candidates")
UIKBRenderFactory10Key = _Class("UIKBRenderFactory10Key")
UIKBRenderFactoryiPad10Key_Portrait = _Class("UIKBRenderFactoryiPad10Key_Portrait")
UIKBRenderFactoryiPad10Key_Landscape = _Class("UIKBRenderFactoryiPad10Key_Landscape")
UIKBRenderFactory10Key_Round = _Class("UIKBRenderFactory10Key_Round")
UIKBRenderFactoryiPadHWR_Portrait = _Class("UIKBRenderFactoryiPadHWR_Portrait")
UIKBRenderFactoryiPadHWR_PortraitFudge = _Class(
    "UIKBRenderFactoryiPadHWR_PortraitFudge"
)
UIKBRenderFactoryiPadHWR_PortraitSansHomeButton = _Class(
    "UIKBRenderFactoryiPadHWR_PortraitSansHomeButton"
)
UIKBRenderFactoryiPadHWR_Landscape = _Class("UIKBRenderFactoryiPadHWR_Landscape")
UIKBRenderFactoryiPadHWR_LandscapeFudge = _Class(
    "UIKBRenderFactoryiPadHWR_LandscapeFudge"
)
UIKBRenderFactoryiPadHWR_LandscapeSansHomeButton = _Class(
    "UIKBRenderFactoryiPadHWR_LandscapeSansHomeButton"
)
UIKBRenderFactory50On_Portrait = _Class("UIKBRenderFactory50On_Portrait")
UIKBRenderFactory50On_Landscape = _Class("UIKBRenderFactory50On_Landscape")
UIKBRenderFactoryHWR_Portrait = _Class("UIKBRenderFactoryHWR_Portrait")
UIKBRenderFactoryHWR_Floating = _Class("UIKBRenderFactoryHWR_Floating")
UIKBRenderFactoryHWR_Landscape = _Class("UIKBRenderFactoryHWR_Landscape")
UIKBRenderFactoryHWR_PortraitTruffle = _Class("UIKBRenderFactoryHWR_PortraitTruffle")
UIKBRenderFactoryHWR_PortraitChoco = _Class("UIKBRenderFactoryHWR_PortraitChoco")
UIKBRenderFactory10Key_Portrait = _Class("UIKBRenderFactory10Key_Portrait")
UIKBRenderFactory10Key_Landscape = _Class("UIKBRenderFactory10Key_Landscape")
UIKBRenderFactory10Key_LandscapeTruffle = _Class(
    "UIKBRenderFactory10Key_LandscapeTruffle"
)
UIKBRenderFactory10Key_LandscapeChoco = _Class("UIKBRenderFactory10Key_LandscapeChoco")
UIKBRenderFactory10Key_PortraitTruffle = _Class(
    "UIKBRenderFactory10Key_PortraitTruffle"
)
UIKBRenderFactory10Key_PortraitChoco = _Class("UIKBRenderFactory10Key_PortraitChoco")
UIKBRenderFactoryNumberPad = _Class("UIKBRenderFactoryNumberPad")
UIKBRenderFactoryNumberPadLandscape = _Class("UIKBRenderFactoryNumberPadLandscape")
UIKBRenderFactoryiPhone = _Class("UIKBRenderFactoryiPhone")
UIKBRenderFactory_Composite = _Class("UIKBRenderFactory_Composite")
UIKBRenderFactory_iPhoneTruffleReachable = _Class(
    "UIKBRenderFactory_iPhoneTruffleReachable"
)
UIKBRenderFactory_iPhoneChocoReachable = _Class(
    "UIKBRenderFactory_iPhoneChocoReachable"
)
UIKBRenderFactoryiPhonePasscode = _Class("UIKBRenderFactoryiPhonePasscode")
UIKBRenderFactoryiPhonePasscodeTruffle = _Class(
    "UIKBRenderFactoryiPhonePasscodeTruffle"
)
UIKBRenderFactoryiPhonePasscodeChoco = _Class("UIKBRenderFactoryiPhonePasscodeChoco")
UIKBRenderFactoryiPhoneTruffle = _Class("UIKBRenderFactoryiPhoneTruffle")
UIKBRenderFactoryiPhoneChoco = _Class("UIKBRenderFactoryiPhoneChoco")
UIKBRenderFactoryiPhoneLandscape = _Class("UIKBRenderFactoryiPhoneLandscape")
UIKBRenderFactoryiPhoneTruffleLandscape = _Class(
    "UIKBRenderFactoryiPhoneTruffleLandscape"
)
UIKBRenderFactoryiPhoneChocoLandscape = _Class("UIKBRenderFactoryiPhoneChocoLandscape")
UIKBRenderFactoryiPad = _Class("UIKBRenderFactoryiPad")
UIKBRenderFactoryiPadPasscode = _Class("UIKBRenderFactoryiPadPasscode")
UIKBRenderFactoryiPadSplit = _Class("UIKBRenderFactoryiPadSplit")
UIKBRenderFactoryiPadSansHomeButton = _Class("UIKBRenderFactoryiPadSansHomeButton")
UIKBRenderFactoryiPadSansHomeButtonLandscape = _Class(
    "UIKBRenderFactoryiPadSansHomeButtonLandscape"
)
UIKBRenderFactoryiPadFudge = _Class("UIKBRenderFactoryiPadFudge")
UIKBRenderFactoryiPadFudgePasscode = _Class("UIKBRenderFactoryiPadFudgePasscode")
UIKBRenderFactoryiPadFudgeLandscape = _Class("UIKBRenderFactoryiPadFudgeLandscape")
UIKBRenderFactoryiPadFudgeLandscapePasscode = _Class(
    "UIKBRenderFactoryiPadFudgeLandscapePasscode"
)
UIKBRenderFactoryiPadLandscape = _Class("UIKBRenderFactoryiPadLandscape")
UIKBRenderFactoryiPadLandscapePasscode = _Class(
    "UIKBRenderFactoryiPadLandscapePasscode"
)
UIInputSwitcher = _Class("UIInputSwitcher")
UITextInputMode = _Class("UITextInputMode")
UIKeyboardInputMode = _Class("UIKeyboardInputMode")
UIKeyboardExtensionInputMode = _Class("UIKeyboardExtensionInputMode")
UIKeyboardSuggestedInputMode = _Class("UIKeyboardSuggestedInputMode")
UISpecializedInputMode = _Class("UISpecializedInputMode")
UIDictationInputMode = _Class("UIDictationInputMode")
UIKBScreenTraits = _Class("UIKBScreenTraits")
UIKeyboardPreferencesController = _Class("UIKeyboardPreferencesController")
UIInputWindowControllerHostingItem = _Class("UIInputWindowControllerHostingItem")
UIInputWindowControllerHosting = _Class("UIInputWindowControllerHosting")
_UIButtonBarButtonVisualProvider = _Class("_UIButtonBarButtonVisualProvider")
_UIButtonBarButtonVisualProviderCarPlay = _Class(
    "_UIButtonBarButtonVisualProviderCarPlay"
)
_UIButtonBarButtonVisualProviderIOS = _Class("_UIButtonBarButtonVisualProviderIOS")
_UIUCBBarButtonVisualProviderIOS = _Class("_UIUCBBarButtonVisualProviderIOS")
_UIUCBPopoverBarButtonVisualProviderIOS = _Class(
    "_UIUCBPopoverBarButtonVisualProviderIOS"
)
_UIUCBGroupBarButtonVisualProviderIOS = _Class("_UIUCBGroupBarButtonVisualProviderIOS")
UIKBRenderConfig = _Class("UIKBRenderConfig")
UIInputViewSetPlacement = _Class("UIInputViewSetPlacement")
UIInputViewSetPlacementInvisible = _Class("UIInputViewSetPlacementInvisible")
UIInputViewSetPlacementInvisibleForFloatingTransition = _Class(
    "UIInputViewSetPlacementInvisibleForFloatingTransition"
)
UIInputViewSetPlacementOffScreenLeftOrRight = _Class(
    "UIInputViewSetPlacementOffScreenLeftOrRight"
)
UIInputViewSetPlacementOffScreenRight = _Class("UIInputViewSetPlacementOffScreenRight")
UIInputViewSetPlacementOffScreenLeft = _Class("UIInputViewSetPlacementOffScreenLeft")
UIInputViewSetPlacementOffScreenDownByScreenHeight = _Class(
    "UIInputViewSetPlacementOffScreenDownByScreenHeight"
)
UIInputViewSetPlacementUndocked = _Class("UIInputViewSetPlacementUndocked")
UIInputViewSetPlacementPlaceholderUndocked = _Class(
    "UIInputViewSetPlacementPlaceholderUndocked"
)
UIInputViewSetPlacementFloating = _Class("UIInputViewSetPlacementFloating")
UIInputViewSetPlacementAssistantOnScreen = _Class(
    "UIInputViewSetPlacementAssistantOnScreen"
)
UIInputViewSetPlacementAccessoryOnScreen = _Class(
    "UIInputViewSetPlacementAccessoryOnScreen"
)
UIInputViewSetPlacementOnScreen = _Class("UIInputViewSetPlacementOnScreen")
UIInputViewSetPlacementPlaceholder = _Class("UIInputViewSetPlacementPlaceholder")
_UIInputViewSetPlacementDragToDismiss = _Class("_UIInputViewSetPlacementDragToDismiss")
UIInputViewSetPlacementOnScreenWithAccessory = _Class(
    "UIInputViewSetPlacementOnScreenWithAccessory"
)
UIInputViewSetPlacementOffScreenDown = _Class("UIInputViewSetPlacementOffScreenDown")
UIInputViewSetPlacementInitialPosition = _Class(
    "UIInputViewSetPlacementInitialPosition"
)
UIStoryboardSegueTemplate = _Class("UIStoryboardSegueTemplate")
UIStoryboardUnwindSegueTemplate = _Class("UIStoryboardUnwindSegueTemplate")
UIStoryboardEmbedSegueTemplate = _Class("UIStoryboardEmbedSegueTemplate")
UIStoryboardPreviewingSegueTemplate = _Class("UIStoryboardPreviewingSegueTemplate")
UIStoryboardReplaceSegueTemplate = _Class("UIStoryboardReplaceSegueTemplate")
UIStoryboardPushSegueTemplate = _Class("UIStoryboardPushSegueTemplate")
UIStoryboardModalSegueTemplate = _Class("UIStoryboardModalSegueTemplate")
UIStoryboardPopoverSegueTemplate = _Class("UIStoryboardPopoverSegueTemplate")
UIStoryboardPresentationSegueTemplate = _Class("UIStoryboardPresentationSegueTemplate")
UIStoryboardPopoverPresentationSegueTemplate = _Class(
    "UIStoryboardPopoverPresentationSegueTemplate"
)
UIStoryboardShowSegueTemplate = _Class("UIStoryboardShowSegueTemplate")
UIRemoteInputViewControllerInterface = _Class("UIRemoteInputViewControllerInterface")
UIInputViewControllerInterfaceClient = _Class("UIInputViewControllerInterfaceClient")
_UIFilteredDataSource = _Class("_UIFilteredDataSource")
_UIDictationTelephonyMonitor = _Class("_UIDictationTelephonyMonitor")
UIDictationConnectionPreferences = _Class("UIDictationConnectionPreferences")
UIDictationConnection = _Class("UIDictationConnection")
UIDictationController = _Class("UIDictationController")
UIScribbleInteraction = _Class("UIScribbleInteraction")
_UISearchBarTextFieldTokenCounter = _Class("_UISearchBarTextFieldTokenCounter")
_UITextFieldPaddedMetricsProvider = _Class("_UITextFieldPaddedMetricsProvider")
_UILargeContentViewerItemStoredProperties = _Class(
    "_UILargeContentViewerItemStoredProperties"
)
_UITextInputControllerLayoutManagerConnection = _Class(
    "_UITextInputControllerLayoutManagerConnection"
)
UITextCheckingController = _Class("UITextCheckingController")
UITextPosition = _Class("UITextPosition")
UIWebCaretRectTextPosition = _Class("UIWebCaretRectTextPosition")
UITextPositionImpl = _Class("UITextPositionImpl")
_UITextKitTextPosition = _Class("_UITextKitTextPosition")
UITextRange = _Class("UITextRange")
UITextRangeImpl = _Class("UITextRangeImpl")
_UITextKitTextRange = _Class("_UITextKitTextRange")
UITextInputController = _Class("UITextInputController")
_UIAutoScrollerItemBehavior = _Class("_UIAutoScrollerItemBehavior")
_UIAutoScrollAssistant = _Class("_UIAutoScrollAssistant")
UIFeedbackGenerator = _Class("UIFeedbackGenerator")
_UIModulationFeedbackGenerator = _Class("_UIModulationFeedbackGenerator")
_UIClickFeedbackGenerator = _Class("_UIClickFeedbackGenerator")
_UIButtonFeedbackGenerator = _Class("_UIButtonFeedbackGenerator")
_UIFeedbackButtonBehavior = _Class("_UIFeedbackButtonBehavior")
_UIFeedbackBehavior = _Class("_UIFeedbackBehavior")
_UIClickPresentationFeedbackGenerator = _Class("_UIClickPresentationFeedbackGenerator")
_UIKeyboardFeedbackGenerator = _Class("_UIKeyboardFeedbackGenerator")
_UIFeedbackKeyboardBehavior = _Class("_UIFeedbackKeyboardBehavior")
_UIDragFeedbackGenerator = _Class("_UIDragFeedbackGenerator")
_UIFeedbackDragBehavior = _Class("_UIFeedbackDragBehavior")
_UIDragSnappingFeedbackGenerator = _Class("_UIDragSnappingFeedbackGenerator")
_UIFeedbackDragSnappingBehavior = _Class("_UIFeedbackDragSnappingBehavior")
_UIStatesFeedbackGenerator = _Class("_UIStatesFeedbackGenerator")
_UIFeedbackStatesBehavior = _Class("_UIFeedbackStatesBehavior")
UISelectionFeedbackGenerator = _Class("UISelectionFeedbackGenerator")
_UIFeedbackRetargetBehavior = _Class("_UIFeedbackRetargetBehavior")
UINotificationFeedbackGenerator = _Class("UINotificationFeedbackGenerator")
_UIFeedbackEventBehavior = _Class("_UIFeedbackEventBehavior")
UIImpactFeedbackGenerator = _Class("UIImpactFeedbackGenerator")
_UIFeedbackImpactBehavior = _Class("_UIFeedbackImpactBehavior")
_UIEdgeFeedbackGenerator = _Class("_UIEdgeFeedbackGenerator")
_UIFeedbackEdgeBehavior = _Class("_UIFeedbackEdgeBehavior")
_UIZoomEdgeFeedbackGenerator = _Class("_UIZoomEdgeFeedbackGenerator")
_UIFeedbackZoomEdgeBehavior = _Class("_UIFeedbackZoomEdgeBehavior")
_UIFeedbackGeneratorConfiguration = _Class("_UIFeedbackGeneratorConfiguration")
_UIModulationFeedbackGeneratorConfiguration = _Class(
    "_UIModulationFeedbackGeneratorConfiguration"
)
_UINotificationFeedbackGeneratorConfiguration = _Class(
    "_UINotificationFeedbackGeneratorConfiguration"
)
_UIFeedbackEventBehaviorConfiguration = _Class("_UIFeedbackEventBehaviorConfiguration")
_UIImpactFeedbackGeneratorConfiguration = _Class(
    "_UIImpactFeedbackGeneratorConfiguration"
)
_UIFeedbackImpactBehaviorConfiguration = _Class(
    "_UIFeedbackImpactBehaviorConfiguration"
)
_UIKeyboardFeedbackGeneratorConfiguration = _Class(
    "_UIKeyboardFeedbackGeneratorConfiguration"
)
_UIFeedbackKeyboardBehaviorConfiguration = _Class(
    "_UIFeedbackKeyboardBehaviorConfiguration"
)
_UIStatesFeedbackGeneratorConfiguration = _Class(
    "_UIStatesFeedbackGeneratorConfiguration"
)
_UIStatesFeedbackGeneratorSwipeActionConfiguration = _Class(
    "_UIStatesFeedbackGeneratorSwipeActionConfiguration"
)
_UIFeedbackSwipeActionStatesBehaviorConfiguration = _Class(
    "_UIFeedbackSwipeActionStatesBehaviorConfiguration"
)
_UIStatesFeedbackGeneratorPreviewConfiguration = _Class(
    "_UIStatesFeedbackGeneratorPreviewConfiguration"
)
_UIFeedbackPreviewStatesBehaviorConfiguration = _Class(
    "_UIFeedbackPreviewStatesBehaviorConfiguration"
)
_UIFeedbackGeneratorUserInteractionDrivenConfiguration = _Class(
    "_UIFeedbackGeneratorUserInteractionDrivenConfiguration"
)
_UIClickFeedbackGeneratorConfiguration = _Class(
    "_UIClickFeedbackGeneratorConfiguration"
)
_UIButtonFeedbackGeneratorConfiguration = _Class(
    "_UIButtonFeedbackGeneratorConfiguration"
)
_UIFeedbackButtonBehaviorConfiguration = _Class(
    "_UIFeedbackButtonBehaviorConfiguration"
)
_UISelectionFeedbackGeneratorConfiguration = _Class(
    "_UISelectionFeedbackGeneratorConfiguration"
)
_UIFeedbackRetargetBehaviorConfiguration = _Class(
    "_UIFeedbackRetargetBehaviorConfiguration"
)
_UIClickPresentationFeedbackGeneratorConfiguration = _Class(
    "_UIClickPresentationFeedbackGeneratorConfiguration"
)
_UIDragFeedbackGeneratorConfiguration = _Class("_UIDragFeedbackGeneratorConfiguration")
_UIFeedbackDragBehaviorConfiguration = _Class("_UIFeedbackDragBehaviorConfiguration")
_UIDragSnappingFeedbackGeneratorConfiguration = _Class(
    "_UIDragSnappingFeedbackGeneratorConfiguration"
)
_UIEdgeFeedbackGeneratorConfiguration = _Class("_UIEdgeFeedbackGeneratorConfiguration")
_UIFeedbackEdgeBehaviorConfiguration = _Class("_UIFeedbackEdgeBehaviorConfiguration")
_UIFullFontSize = _Class("_UIFullFontSize")
_UITextFieldPassthroughMetricsProvider = _Class(
    "_UITextFieldPassthroughMetricsProvider"
)
_UITextFieldBackgroundProvider = _Class("_UITextFieldBackgroundProvider")
_UITextFieldDrawingBackgroundProvider = _Class("_UITextFieldDrawingBackgroundProvider")
_UITextFieldLineBackgroundProvider = _Class("_UITextFieldLineBackgroundProvider")
_UITextFieldBezelBackgroundProvider = _Class("_UITextFieldBezelBackgroundProvider")
_UITextFieldViewBackgroundProvider = _Class("_UITextFieldViewBackgroundProvider")
_UITextFieldTVBackgroundProvider = _Class("_UITextFieldTVBackgroundProvider")
_UITextFieldMacBackgroundProvider = _Class("_UITextFieldMacBackgroundProvider")
_UITextFieldImageBackgroundProvider = _Class("_UITextFieldImageBackgroundProvider")
_UITextFieldSystemBackgroundProvider = _Class("_UITextFieldSystemBackgroundProvider")
_UITextFieldPasscodeBackgroundProvider = _Class(
    "_UITextFieldPasscodeBackgroundProvider"
)
_UITextFieldNoBackgroundProvider = _Class("_UITextFieldNoBackgroundProvider")
_UITextFieldVisualStyle = _Class("_UITextFieldVisualStyle")
_UITextFieldVisualStyle_tvOS = _Class("_UITextFieldVisualStyle_tvOS")
_UITextFieldVisualStyle_iOS = _Class("_UITextFieldVisualStyle_iOS")
UIAccessibilityHUDGestureManager = _Class("UIAccessibilityHUDGestureManager")
UILargeContentViewerInteraction = _Class("UILargeContentViewerInteraction")
_UISearchBarLayoutBase = _Class("_UISearchBarLayoutBase")
_UISearchBarScopeContainerLayout = _Class("_UISearchBarScopeContainerLayout")
_UISearchBarSearchContainerLayout = _Class("_UISearchBarSearchContainerLayout")
_UISearchBarLayout = _Class("_UISearchBarLayout")
_UISearchBarVisualProviderIOS = _Class("_UISearchBarVisualProviderIOS")
UITextInputTraits = _Class("UITextInputTraits")
_UITextInputSessionAccumulator = _Class("_UITextInputSessionAccumulator")
UINavigationItem = _Class("UINavigationItem")
_UIDocumentPickerNavigationItem = _Class("_UIDocumentPickerNavigationItem")
_UISearchBarNavigationItem = _Class("_UISearchBarNavigationItem")
_UISceneEventRegistry = _Class("_UISceneEventRegistry")
UIBezierPath = _Class("UIBezierPath")
_UIActivityIndicatorViewArtworkCacheKey = _Class(
    "_UIActivityIndicatorViewArtworkCacheKey"
)
_UIViewLayoutEngineRelativeAlignmentRectOriginCache = _Class(
    "_UIViewLayoutEngineRelativeAlignmentRectOriginCache"
)
_UISceneEventResponse = _Class("_UISceneEventResponse")
_UISimpleFenceProvider = _Class("_UISimpleFenceProvider")
UIApplicationSceneClientSettingsDiffInspector = _Class(
    "UIApplicationSceneClientSettingsDiffInspector"
)
UIApplicationSceneSettingsDiffInspector = _Class(
    "UIApplicationSceneSettingsDiffInspector"
)
_UIFocusUpdateRequest = _Class("_UIFocusUpdateRequest")
_UIAccessibilityFocusUpdateRequest = _Class("_UIAccessibilityFocusUpdateRequest")
UIInputViewAnimationStyle = _Class("UIInputViewAnimationStyle")
_UIKeyboardAnimatorAnimationStyle = _Class("_UIKeyboardAnimatorAnimationStyle")
UIInputViewAnimationStyleDirectional = _Class("UIInputViewAnimationStyleDirectional")
_UIViewControllerKeyboardAnimationStyle = _Class(
    "_UIViewControllerKeyboardAnimationStyle"
)
_UITextInputSessionAction = _Class("_UITextInputSessionAction")
_UITextInputSessionInsertionAction = _Class("_UITextInputSessionInsertionAction")
_UITextInputSessionRedoAction = _Class("_UITextInputSessionRedoAction")
_UITextInputSessionUndoAction = _Class("_UITextInputSessionUndoAction")
_UITextInputSessionSelectionAction = _Class("_UITextInputSessionSelectionAction")
_UITextInputSessionDeletionAction = _Class("_UITextInputSessionDeletionAction")
_UITextInputSessionBeganAction = _Class("_UITextInputSessionBeganAction")
UITextInputSessionActionAnalytics = _Class("UITextInputSessionActionAnalytics")
UIKeyboardInputModeController = _Class("UIKeyboardInputModeController")
_UIScenePointerLockDiffAction = _Class("_UIScenePointerLockDiffAction")
UIPointerLockState = _Class("UIPointerLockState")
UIViewPropertyAnimatorTrackingState = _Class("UIViewPropertyAnimatorTrackingState")
UIViewPropertyAnimator = _Class("UIViewPropertyAnimator")
_UISwipePropertyAnimator = _Class("_UISwipePropertyAnimator")
_UIPanelCoordinatingAnimator = _Class("_UIPanelCoordinatingAnimator")
_UIViewControllerImmediateAnimationTransitionCoordinator = _Class(
    "_UIViewControllerImmediateAnimationTransitionCoordinator"
)
_UISheetPresentationControllerConfiguration = _Class(
    "_UISheetPresentationControllerConfiguration"
)
_UIEventEnvironmentClearTouchesContext = _Class(
    "_UIEventEnvironmentClearTouchesContext"
)
_UIObjectPerCanvas = _Class("_UIObjectPerCanvas")
UITextEffectsHostingInfo = _Class("UITextEffectsHostingInfo")
UIViewControllerBuiltinTransitionViewAnimator = _Class(
    "UIViewControllerBuiltinTransitionViewAnimator"
)
UIBarItem = _Class("UIBarItem")
UITabBarItem = _Class("UITabBarItem")
UIBarButtonItem = _Class("UIBarButtonItem")
UISplitViewControllerDisplayModeBarButtonItem = _Class(
    "UISplitViewControllerDisplayModeBarButtonItem"
)
_UIFloatableBarButtonItem = _Class("_UIFloatableBarButtonItem")
UIFocusRingManager = _Class("UIFocusRingManager")
_UIDelayedPresentationContext = _Class("_UIDelayedPresentationContext")
_UISystemBaselineConstraint = _Class("_UISystemBaselineConstraint")
_UILayoutSupportConstraint = _Class("_UILayoutSupportConstraint")
_UIWindowAutoresizingConstraint = _Class("_UIWindowAutoresizingConstraint")
_UIScrollViewAutomaticContentSizeConstraint = _Class(
    "_UIScrollViewAutomaticContentSizeConstraint"
)
_UIWindowAnchoringConstraint = _Class("_UIWindowAnchoringConstraint")
_UIImageViewExtendedStorage = _Class("_UIImageViewExtendedStorage")
_UIPointerEffectSizeRuleSettings = _Class("_UIPointerEffectSizeRuleSettings")
_UISearchBarBehaviorSettings = _Class("_UISearchBarBehaviorSettings")
_UITabBarBehaviorSettings = _Class("_UITabBarBehaviorSettings")
_UINavigationAndToolbarBehaviorSettings = _Class(
    "_UINavigationAndToolbarBehaviorSettings"
)
_UIButtonBehaviorSettings = _Class("_UIButtonBehaviorSettings")
_UIPointerTextBehaviorSettings = _Class("_UIPointerTextBehaviorSettings")
_UIFreeformPointerSettings = _Class("_UIFreeformPointerSettings")
_UILinkPointerSettings = _Class("_UILinkPointerSettings")
_UIBeamPointerSettings = _Class("_UIBeamPointerSettings")
_UIPointerEffectSettings = _Class("_UIPointerEffectSettings")
_UIPointerSBAppIconEffectSettings = _Class("_UIPointerSBAppIconEffectSettings")
_UIPointerHoverEffectSettings = _Class("_UIPointerHoverEffectSettings")
_UIPointerLiftEffectSettings = _Class("_UIPointerLiftEffectSettings")
_UIPointerHighlightEffectSettings = _Class("_UIPointerHighlightEffectSettings")
_UIPointerSettings = _Class("_UIPointerSettings")
_UIPageControlIndicatorSettings = _Class("_UIPageControlIndicatorSettings")
_UIPageControlPlatterSettings = _Class("_UIPageControlPlatterSettings")
_UIPageControlSettings = _Class("_UIPageControlSettings")
_UISettings = _Class("_UISettings")
_UIMotionAnalyzerSettings = _Class("_UIMotionAnalyzerSettings")
_UIScreenEdgePanRecognizerCornerSettings = _Class(
    "_UIScreenEdgePanRecognizerCornerSettings"
)
_UIScreenEdgePanRecognizerDwellSettings = _Class(
    "_UIScreenEdgePanRecognizerDwellSettings"
)
_UIScreenEdgePanRecognizerEdgeSettings = _Class(
    "_UIScreenEdgePanRecognizerEdgeSettings"
)
_UIScreenEdgePanRecognizerSettings = _Class("_UIScreenEdgePanRecognizerSettings")
_UITextSelectionSettings = _Class("_UITextSelectionSettings")
_UIActivityIndicatorSettings = _Class("_UIActivityIndicatorSettings")
_UIPageControlSettingsDomain = _Class("_UIPageControlSettingsDomain")
_UIPointerSettingsDomain = _Class("_UIPointerSettingsDomain")
_UIActivityIndicatorSettingsDomain = _Class("_UIActivityIndicatorSettingsDomain")
UILayoutGuide = _Class("UILayoutGuide")
_UIScrollViewLayoutGuide = _Class("_UIScrollViewLayoutGuide")
_UIContentConstraintsLayoutGuide = _Class("_UIContentConstraintsLayoutGuide")
_UILayoutSpacer = _Class("_UILayoutSpacer")
_UIOLAGapGuide = _Class("_UIOLAGapGuide")
_UIScrollViewContentOffsetGuide = _Class("_UIScrollViewContentOffsetGuide")
UIFocusGuide = _Class("UIFocusGuide")
UIKBFocusGuide = _Class("UIKBFocusGuide")
UIFocusContainerGuide = _Class("UIFocusContainerGuide")
UIViewAnimationBlockDelegate = _Class("UIViewAnimationBlockDelegate")
UIViewAnimationState = _Class("UIViewAnimationState")
UIViewKeyframeAnimationState = _Class("UIViewKeyframeAnimationState")
UIViewInProcessAnimationState = _Class("UIViewInProcessAnimationState")
UIViewPropertyCollectingAnimationState = _Class(
    "UIViewPropertyCollectingAnimationState"
)
UIViewSpringAnimationState = _Class("UIViewSpringAnimationState")
UIStatusBarAnimationParameters = _Class("UIStatusBarAnimationParameters")
UIStatusBarHideAnimationParameters = _Class("UIStatusBarHideAnimationParameters")
UIStatusBarStyleAnimationParameters = _Class("UIStatusBarStyleAnimationParameters")
UIStatusBarOrientationAnimationParameters = _Class(
    "UIStatusBarOrientationAnimationParameters"
)
_UIScreenFixedCoordinateSpace = _Class("_UIScreenFixedCoordinateSpace")
_UIViewControllerTransitionCoordinator = _Class(
    "_UIViewControllerTransitionCoordinator"
)
_UIWindowAnimationController = _Class("_UIWindowAnimationController")
_UIHostedWindowAnimationController = _Class("_UIHostedWindowAnimationController")
_UIWindowRotationAnimationController = _Class("_UIWindowRotationAnimationController")
_UIViewControllerTransitionContext = _Class("_UIViewControllerTransitionContext")
_UIViewControllerOneToOneTransitionContext = _Class(
    "_UIViewControllerOneToOneTransitionContext"
)
UIOpenURLContext = _Class("UIOpenURLContext")
_UISelectorDictionary = _Class("_UISelectorDictionary")
_UICommandIdentifierDictionary = _Class("_UICommandIdentifierDictionary")
_UIMenuBuilder = _Class("_UIMenuBuilder")
UIMenuSystem = _Class("UIMenuSystem")
UIMenuElement = _Class("UIMenuElement")
UIDeferredMenuElement = _Class("UIDeferredMenuElement")
UIAction = _Class("UIAction")
_UIImmutableAction = _Class("_UIImmutableAction")
UIMenu = _Class("UIMenu")
UICommand = _Class("UICommand")
_UIImmutableCommand = _Class("_UIImmutableCommand")
_UIValidatableCommand = _Class("_UIValidatableCommand")
UIKeyCommand = _Class("UIKeyCommand")
_UIImmutableKeyCommand = _Class("_UIImmutableKeyCommand")
_UIWindowOrientationUpdate = _Class("_UIWindowOrientationUpdate")
_UISheetDetent = _Class("_UISheetDetent")
_UISheetLayoutInfo = _Class("_UISheetLayoutInfo")
UIPresentationController = _Class("UIPresentationController")
_UIPreviewPlatterPresentationController = _Class(
    "_UIPreviewPlatterPresentationController"
)
_UISearchFormSheetPresentationController = _Class(
    "_UISearchFormSheetPresentationController"
)
_UISearchPresentationController = _Class("_UISearchPresentationController")
_UISearchCarPlayPresentationController = _Class(
    "_UISearchCarPlayPresentationController"
)
_UISearchATVPresentationController = _Class("_UISearchATVPresentationController")
UIKeyboardVCPresentationController = _Class("UIKeyboardVCPresentationController")
_UIProgressiveBlurPresentationController = _Class(
    "_UIProgressiveBlurPresentationController"
)
_UIActionSheetCompactPresentationController = _Class(
    "_UIActionSheetCompactPresentationController"
)
_UIAlertControllerPresentationController = _Class(
    "_UIAlertControllerPresentationController"
)
_UIAlertControllerActionSheetCompactPresentationController = _Class(
    "_UIAlertControllerActionSheetCompactPresentationController"
)
_UIAlertControllerAlertPresentationController = _Class(
    "_UIAlertControllerAlertPresentationController"
)
_UICurrentContextPresentationController = _Class(
    "_UICurrentContextPresentationController"
)
_UIOverCurrentContextPresentationController = _Class(
    "_UIOverCurrentContextPresentationController"
)
_UIFullscreenPresentationController = _Class("_UIFullscreenPresentationController")
_UIOverFullscreenPresentationController = _Class(
    "_UIOverFullscreenPresentationController"
)
UIPreviewPresentationController = _Class("UIPreviewPresentationController")
_UIPreviewPresentationController = _Class("_UIPreviewPresentationController")
_UIPreviewPresentationController2 = _Class("_UIPreviewPresentationController2")
UIPopoverPresentationController = _Class("UIPopoverPresentationController")
_UISharingViewPresentationController = _Class("_UISharingViewPresentationController")
_UISearchPopoverPresentationController = _Class(
    "_UISearchPopoverPresentationController"
)
_UIActionSheetPresentationController = _Class("_UIActionSheetPresentationController")
_UIAlertControllerActionSheetRegularPresentationController = _Class(
    "_UIAlertControllerActionSheetRegularPresentationController"
)
_UISheetPresentationController = _Class("_UISheetPresentationController")
_UIFormSheetPresentationController = _Class("_UIFormSheetPresentationController")
_UIPageSheetPresentationController = _Class("_UIPageSheetPresentationController")
_UIRootPresentationController = _Class("_UIRootPresentationController")
UICustomObject = _Class("UICustomObject")
UIStoryboardDecodingContext = _Class("UIStoryboardDecodingContext")
UIClassSwapper = _Class("UIClassSwapper")
UIProxyObject = _Class("UIProxyObject")
UIRuntimeConnection = _Class("UIRuntimeConnection")
UIRuntimeOutletCollectionConnection = _Class("UIRuntimeOutletCollectionConnection")
UIRuntimeEventConnection = _Class("UIRuntimeEventConnection")
UIRuntimeOutletConnection = _Class("UIRuntimeOutletConnection")
UIStoryboardScene = _Class("UIStoryboardScene")
UINibStorage = _Class("UINibStorage")
UINib = _Class("UINib")
UITextFormattingCoordinator = _Class("UITextFormattingCoordinator")
UIInputViewSet = _Class("UIInputViewSet")
_UIWindowSceneStatusBarSettingsDiffAction = _Class(
    "_UIWindowSceneStatusBarSettingsDiffAction"
)
_UIFocusSystemSceneComponent = _Class("_UIFocusSystemSceneComponent")
_UIFocusSystemKeyboardSceneComponent = _Class("_UIFocusSystemKeyboardSceneComponent")
UIAlertControllerStackManager = _Class("UIAlertControllerStackManager")
_UIBannerManager = _Class("_UIBannerManager")
_UISystemAppearanceManager = _Class("_UISystemAppearanceManager")
UIStatusBarManager = _Class("UIStatusBarManager")
_UIWindowSceneCoordinateSpace = _Class("_UIWindowSceneCoordinateSpace")
_UIScenefbsSceneBasedMetricsCalculator = _Class(
    "_UIScenefbsSceneBasedMetricsCalculator"
)
_UIContextBinder = _Class("_UIContextBinder")
_UIContextBinderSubstrate = _Class("_UIContextBinderSubstrate")
_UINullSubstrate = _Class("_UINullSubstrate")
_UIFBSSceneSubstrate = _Class("_UIFBSSceneSubstrate")
_UISceneLifecycleMonitor = _Class("_UISceneLifecycleMonitor")
_UIWindowSceneFBSSceneLifecycleMonitor = _Class(
    "_UIWindowSceneFBSSceneLifecycleMonitor"
)
_UIWindowHostingSceneSafeAreaInsetsSettingsDiffAction = _Class(
    "_UIWindowHostingSceneSafeAreaInsetsSettingsDiffAction"
)
_UIWindowSceneOcclusionSettingsDiffAction = _Class(
    "_UIWindowSceneOcclusionSettingsDiffAction"
)
_UIWindowSceneGeometrySettingsDiffAction = _Class(
    "_UIWindowSceneGeometrySettingsDiffAction"
)
_UIWindowSceneDeviceOrientationSettingsDiffAction = _Class(
    "_UIWindowSceneDeviceOrientationSettingsDiffAction"
)
_UIWindowSceneUserInterfaceStyleSettingsDiffAction = _Class(
    "_UIWindowSceneUserInterfaceStyleSettingsDiffAction"
)
_UIWindowSceneFBSSceneTransitionContextDrivenLifecycleSettingsDiffAction = _Class(
    "_UIWindowSceneFBSSceneTransitionContextDrivenLifecycleSettingsDiffAction"
)
_UIWindowSceneDisplayConfigurationSettingsDiffAction = _Class(
    "_UIWindowSceneDisplayConfigurationSettingsDiffAction"
)
UISceneActivationConditions = _Class("UISceneActivationConditions")
UISceneConnectionOptions = _Class("UISceneConnectionOptions")
_UISceneConnectionOptionsContext = _Class("_UISceneConnectionOptionsContext")
_UISceneApplicationActionsHandler = _Class("_UISceneApplicationActionsHandler")
_UICanvasApplicationSceneActionsHandler = _Class(
    "_UICanvasApplicationSceneActionsHandler"
)
_UISceneSnapshotBSActionsHandler = _Class("_UISceneSnapshotBSActionsHandler")
_UISceneCloudKitShareMetadataBSActionHandler = _Class(
    "_UISceneCloudKitShareMetadataBSActionHandler"
)
_UISceneShortcutItemBSActionsHandler = _Class("_UISceneShortcutItemBSActionsHandler")
_UISceneUserNotificationsBSActionsHandler = _Class(
    "_UISceneUserNotificationsBSActionsHandler"
)
_UISceneOpenURLBSActionsHandler = _Class("_UISceneOpenURLBSActionsHandler")
_UISceneUserActivityBSActionsHandler = _Class("_UISceneUserActivityBSActionsHandler")
UIStoryboard = _Class("UIStoryboard")
UISceneConfiguration = _Class("UISceneConfiguration")
UISceneSession = _Class("UISceneSession")
_UICanvasDefinition = _Class("_UICanvasDefinition")
_UIMutableCanvasDefinition = _Class("_UIMutableCanvasDefinition")
_UIWeakReference = _Class("_UIWeakReference")
_UIBoxedAutoreleasePoolMark = _Class("_UIBoxedAutoreleasePoolMark")
_UIAfterCACommitBlock = _Class("_UIAfterCACommitBlock")
_UIObjectReferenceCounter = _Class("_UIObjectReferenceCounter")
_UIBackgroundTaskInfo = _Class("_UIBackgroundTaskInfo")
UIPasteboard = _Class("UIPasteboard")
_UIConcretePasteboard = _Class("_UIConcretePasteboard")
_UIImageContentRendition = _Class("_UIImageContentRendition")
_UIImageContentContextualEffect = _Class("_UIImageContentContextualEffect")
_UIImageContentLayout = _Class("_UIImageContentLayout")
_UIImageContentLayoutDrawingTarget = _Class("_UIImageContentLayoutDrawingTarget")
UIGraphicsRendererContext = _Class("UIGraphicsRendererContext")
UIGraphicsPDFRendererContext = _Class("UIGraphicsPDFRendererContext")
UIGraphicsImageRendererContext = _Class("UIGraphicsImageRendererContext")
_UIReusePool = _Class("_UIReusePool")
UIGraphicsRenderer = _Class("UIGraphicsRenderer")
UIGraphicsPDFRenderer = _Class("UIGraphicsPDFRenderer")
UIGraphicsImageRenderer = _Class("UIGraphicsImageRenderer")
UIGraphicsRendererFormat = _Class("UIGraphicsRendererFormat")
UIGraphicsPDFRendererFormat = _Class("UIGraphicsPDFRendererFormat")
UIGraphicsImageRendererFormat = _Class("UIGraphicsImageRendererFormat")
_UIFieldEditorLayoutManager = _Class("_UIFieldEditorLayoutManager")
_UILabelContent = _Class("_UILabelContent")
_UILabelAttributedStringContent = _Class("_UILabelAttributedStringContent")
_UILabelStringContent = _Class("_UILabelStringContent")
_UITextAttributeDefaultCategories = _Class("_UITextAttributeDefaultCategories")
_UITextAttributeDefaults = _Class("_UITextAttributeDefaults")
_UILabelVisualStyle = _Class("_UILabelVisualStyle")
_UILabelVisualStyle_tvOS = _Class("_UILabelVisualStyle_tvOS")
_UILabelVisualStyle_iOS = _Class("_UILabelVisualStyle_iOS")
UIFocusSystem = _Class("UIFocusSystem")
_UIHostedFocusSystem = _Class("_UIHostedFocusSystem")
UIButtonContent = _Class("UIButtonContent")
UIControlTargetAction = _Class("UIControlTargetAction")
_UIPointerArbiterCore_iOS = _Class("_UIPointerArbiterCore_iOS")
_UIPointerArbiter = _Class("_UIPointerArbiter")
UIGestureGraphElement = _Class("UIGestureGraphElement")
UIGestureGraphEdge = _Class("UIGestureGraphEdge")
UIGestureGraphNode = _Class("UIGestureGraphNode")
UITapRecognizer = _Class("UITapRecognizer")
UIGestureRecognizerTarget = _Class("UIGestureRecognizerTarget")
UIGestureRecognizer = _Class("UIGestureRecognizer")
_UIContextMenuActionScrubbingHandoffGestureRecognizer = _Class(
    "_UIContextMenuActionScrubbingHandoffGestureRecognizer"
)
UIDragRecognizer = _Class("UIDragRecognizer")
_UIFocusLinearMovementDebugGestureRecognizer = _Class(
    "_UIFocusLinearMovementDebugGestureRecognizer"
)
_UIStatusBarActionGestureRecognizer = _Class("_UIStatusBarActionGestureRecognizer")
_UITouchDownGestureRecognizer = _Class("_UITouchDownGestureRecognizer")
_UISteadyTouchForceGestureRecognizer = _Class("_UISteadyTouchForceGestureRecognizer")
_UIPreviewInteractionFailureRelationshipGestureRecognizer = _Class(
    "_UIPreviewInteractionFailureRelationshipGestureRecognizer"
)
_UIGestureStudyMetricsGestureRecognizer = _Class(
    "_UIGestureStudyMetricsGestureRecognizer"
)
_UITouchesObservingGestureRecognizer = _Class("_UITouchesObservingGestureRecognizer")
_UIPreviewInteractionTouchObservingGestureRecognizer = _Class(
    "_UIPreviewInteractionTouchObservingGestureRecognizer"
)
_UIKeyboardTextSelectionTouchesObservingGestureRecognizer = _Class(
    "_UIKeyboardTextSelectionTouchesObservingGestureRecognizer"
)
_UIPassthroughGateGestureRecognizer = _Class("_UIPassthroughGateGestureRecognizer")
_UIInterruptScrollDecelerationGestureRecognizer = _Class(
    "_UIInterruptScrollDecelerationGestureRecognizer"
)
UITouchForceGestureRecognizer = _Class("UITouchForceGestureRecognizer")
UIDigitizerLongPressGestureRecognizer = _Class("UIDigitizerLongPressGestureRecognizer")
UIDigitizerTapGestureRecognizer = _Class("UIDigitizerTapGestureRecognizer")
_UIDirectTouchObserverGestureRecognizer = _Class(
    "_UIDirectTouchObserverGestureRecognizer"
)
UIImmediateEdgeSwipeGestureRecognizer = _Class("UIImmediateEdgeSwipeGestureRecognizer")
_UIPendingEdgeSwipeGestureRecognizer = _Class("_UIPendingEdgeSwipeGestureRecognizer")
_UIExclusiveTouchGestureRecognizer = _Class("_UIExclusiveTouchGestureRecognizer")
UIHBLongClickGestureRecognizer = _Class("UIHBLongClickGestureRecognizer")
UIHBDownGestureRecognizer = _Class("UIHBDownGestureRecognizer")
UIHBClickGestureRecognizer = _Class("UIHBClickGestureRecognizer")
_UIFocusPressGestureRecognizer = _Class("_UIFocusPressGestureRecognizer")
_UIRepeatingPressGestureRecognizer = _Class("_UIRepeatingPressGestureRecognizer")
UIScrollViewDirectionalPressGestureRecognizer = _Class(
    "UIScrollViewDirectionalPressGestureRecognizer"
)
_UIFocusEngineRepeatingPressGestureRecognizer = _Class(
    "_UIFocusEngineRepeatingPressGestureRecognizer"
)
_UIFocusEngineJoystickGestureRecognizer = _Class(
    "_UIFocusEngineJoystickGestureRecognizer"
)
_UIContextMenuSelectionGestureRecognizer = _Class(
    "_UIContextMenuSelectionGestureRecognizer"
)
_UITrackingGestureRecognizer = _Class("_UITrackingGestureRecognizer")
_UITabBarTouchDetectionGestureRecognizer = _Class(
    "_UITabBarTouchDetectionGestureRecognizer"
)
_UIContextMenuSelectionDelayGestureRecognizer = _Class(
    "_UIContextMenuSelectionDelayGestureRecognizer"
)
_UIInterfaceActionSelectionDelayGestureRecognizer = _Class(
    "_UIInterfaceActionSelectionDelayGestureRecognizer"
)
UIWebTouchEventsGestureRecognizer = _Class("UIWebTouchEventsGestureRecognizer")
UIKeyboardPinchGestureRecognizer = _Class("UIKeyboardPinchGestureRecognizer")
UIScrollViewPagingSwipeGestureRecognizer = _Class(
    "UIScrollViewPagingSwipeGestureRecognizer"
)
_UIPassthroughScrollGestureRecognizer = _Class("_UIPassthroughScrollGestureRecognizer")
_UISwipeDismissalGestureRecognizer = _Class("_UISwipeDismissalGestureRecognizer")
UITextMultiTapRecognizer = _Class("UITextMultiTapRecognizer")
UITapAndAHalfRecognizer = _Class("UITapAndAHalfRecognizer")
_UITouchDurationObservingGestureRecognizer = _Class(
    "_UITouchDurationObservingGestureRecognizer"
)
_UIContextualMenuGestureRecognizer = _Class("_UIContextualMenuGestureRecognizer")
_UISecondaryClickDriverGestureRecognizer = _Class(
    "_UISecondaryClickDriverGestureRecognizer"
)
_UIRelationshipGestureRecognizer = _Class("_UIRelationshipGestureRecognizer")
UIRotationGestureRecognizer = _Class("UIRotationGestureRecognizer")
UIPinchGestureRecognizer = _Class("UIPinchGestureRecognizer")
UIScrollViewPinchGestureRecognizer = _Class("UIScrollViewPinchGestureRecognizer")
UIKeyboardFloatingPinchGestureRecognizer = _Class(
    "UIKeyboardFloatingPinchGestureRecognizer"
)
UIKBProductivityPinchGestureRecognizer = _Class(
    "UIKBProductivityPinchGestureRecognizer"
)
UIUndoGestureObserver = _Class("UIUndoGestureObserver")
UIDragGestureRecognizer = _Class("UIDragGestureRecognizer")
UISpringLoadedGestureRecognizer = _Class("UISpringLoadedGestureRecognizer")
UIDropInteractionGestureRecognizer = _Class("UIDropInteractionGestureRecognizer")
_UIDragAutoScrollGestureRecognizer = _Class("_UIDragAutoScrollGestureRecognizer")
UIPanGestureRecognizer = _Class("UIPanGestureRecognizer")
_UIFocusEnginePanGestureRecognizer = _Class("_UIFocusEnginePanGestureRecognizer")
_UIBarPanGestureRecognizer = _Class("_UIBarPanGestureRecognizer")
UITextRangeAdjustmentGestureRecognizer = _Class(
    "UITextRangeAdjustmentGestureRecognizer"
)
_UISwipeActionPanGestureRecognizer = _Class("_UISwipeActionPanGestureRecognizer")
_UIMultiSelectOneFingerPanGesture = _Class("_UIMultiSelectOneFingerPanGesture")
UITextLoupePanGestureRecognizer = _Class("UITextLoupePanGestureRecognizer")
_UIPanOrFlickGestureRecognizer = _Class("_UIPanOrFlickGestureRecognizer")
_UIEditableTextSelectionTwoFingerPanGesture = _Class(
    "_UIEditableTextSelectionTwoFingerPanGesture"
)
UIScreenEdgePanGestureRecognizer = _Class("UIScreenEdgePanGestureRecognizer")
_UIParallaxTransitionPanGestureRecognizer = _Class(
    "_UIParallaxTransitionPanGestureRecognizer"
)
UIKBProductivityPanGestureRecognizer = _Class("UIKBProductivityPanGestureRecognizer")
UIScrollViewPanGestureRecognizer = _Class("UIScrollViewPanGestureRecognizer")
UIScrollViewDelayedTouchesBeganGestureRecognizer = _Class(
    "UIScrollViewDelayedTouchesBeganGestureRecognizer"
)
UITapGestureRecognizer = _Class("UITapGestureRecognizer")
_UIEditableTextSelectionTwoFingerTapGesture = _Class(
    "_UIEditableTextSelectionTwoFingerTapGesture"
)
_CarButtonTapGestureRecognizer = _Class("_CarButtonTapGestureRecognizer")
_UIDismissCurlUpTapGestureRecognizer = _Class("_UIDismissCurlUpTapGestureRecognizer")
_UIBarTapGestureRecognizer = _Class("_UIBarTapGestureRecognizer")
_UIInterfaceActionSelectByPressGestureRecognizer = _Class(
    "_UIInterfaceActionSelectByPressGestureRecognizer"
)
_UISingleFingerTapExtensionGesture = _Class("_UISingleFingerTapExtensionGesture")
UITextTapRecognizer = _Class("UITextTapRecognizer")
UISelectionTapRecognizer = _Class("UISelectionTapRecognizer")
_UIDragAddItemsGesture = _Class("_UIDragAddItemsGesture")
UIKBProductivityDoubleTapGesture = _Class("UIKBProductivityDoubleTapGesture")
UIKBProductivitySingleTapGesture = _Class("UIKBProductivitySingleTapGesture")
_UISystemGestureGateGestureRecognizer = _Class("_UISystemGestureGateGestureRecognizer")
UISwipeGestureRecognizer = _Class("UISwipeGestureRecognizer")
UILongPressGestureRecognizer = _Class("UILongPressGestureRecognizer")
_UITouchObservingLongPress = _Class("_UITouchObservingLongPress")
_UIPreviewInteractionGestureRecognizer = _Class(
    "_UIPreviewInteractionGestureRecognizer"
)
_UITextSelectionForceGesture = _Class("_UITextSelectionForceGesture")
_UINonEditableTextSelectionForceGesture = _Class(
    "_UINonEditableTextSelectionForceGesture"
)
_UIEditableTextSelectionForceGesture = _Class("_UIEditableTextSelectionForceGesture")
UIPhraseBoundaryGestureRecognizer = _Class("UIPhraseBoundaryGestureRecognizer")
_UIWebHighlightLongPressGestureRecognizer = _Class(
    "_UIWebHighlightLongPressGestureRecognizer"
)
_UIRevealGestureRecognizer = _Class("_UIRevealGestureRecognizer")
_UIPreviewGestureRecognizer = _Class("_UIPreviewGestureRecognizer")
UIVariableDelayLoupeGesture = _Class("UIVariableDelayLoupeGesture")
_UIDragLiftGestureRecognizer = _Class("_UIDragLiftGestureRecognizer")
_UIDragLiftPointerGestureRecognizer = _Class("_UIDragLiftPointerGestureRecognizer")
_UIDragLiftPointerWithEarlyStartGestureRecognizer = _Class(
    "_UIDragLiftPointerWithEarlyStartGestureRecognizer"
)
UIKBProductivityLongPressGestureRecognizer = _Class(
    "UIKBProductivityLongPressGestureRecognizer"
)
UIScrollViewKnobLongPressGestureRecognizer = _Class(
    "UIScrollViewKnobLongPressGestureRecognizer"
)
UIAccessibilityHUDGestureLongPressRecognizer = _Class(
    "UIAccessibilityHUDGestureLongPressRecognizer"
)
_UIPointerInteractionPressGestureRecognizer = _Class(
    "_UIPointerInteractionPressGestureRecognizer"
)
UIHoverGestureRecognizer = _Class("UIHoverGestureRecognizer")
_UIPointerInteractionHoverGestureRecognizer = _Class(
    "_UIPointerInteractionHoverGestureRecognizer"
)
UISpringLoadedInteraction = _Class("UISpringLoadedInteraction")
_UIPointerInteractionHoverDriver = _Class("_UIPointerInteractionHoverDriver")
UIPointerInteraction = _Class("UIPointerInteraction")
_UIPointerInteractionAssistant = _Class("_UIPointerInteractionAssistant")
UIImage = _Class("UIImage")
_UIStatusBarImage = _Class("_UIStatusBarImage")
UIImageNibPlaceholder = _Class("UIImageNibPlaceholder")
_UIMappedBitmapImage = _Class("_UIMappedBitmapImage")
_UIAnimatedImage = _Class("_UIAnimatedImage")
_UISegmentedControlDividerImage = _Class("_UISegmentedControlDividerImage")
_UIResizableImage = _Class("_UIResizableImage")
UIKBCachedImage = _Class("UIKBCachedImage")
_UIImageContent = _Class("_UIImageContent")
_UIImageMultiVectorGlyphContent = _Class("_UIImageMultiVectorGlyphContent")
_UIImageCGSVGDocumentContent = _Class("_UIImageCGSVGDocumentContent")
_UIImageCGPDFPageContent = _Class("_UIImageCGPDFPageContent")
_UIImageIOSurfaceContent = _Class("_UIImageIOSurfaceContent")
_UIImageCIImageContent = _Class("_UIImageCIImageContent")
_UIImageEmptyContent = _Class("_UIImageEmptyContent")
_UIImageCGImageContent = _Class("_UIImageCGImageContent")
_UIImageAsyncCGImageContent = _Class("_UIImageAsyncCGImageContent")
_UIImageCUIVectorGlyphContent = _Class("_UIImageCUIVectorGlyphContent")
_UIImageCUIVectorImageContent = _Class("_UIImageCUIVectorImageContent")
_UIImageAssetMapEnvelope = _Class("_UIImageAssetMapEnvelope")
UIImageAsset = _Class("UIImageAsset")
_UIImageStackImageAsset = _Class("_UIImageStackImageAsset")
_UIPathLazyImageAsset = _Class("_UIPathLazyImageAsset")
_UIImageCacheKey = _Class("_UIImageCacheKey")
_UIAssetManager = _Class("_UIAssetManager")
UIImageConfiguration = _Class("UIImageConfiguration")
UIImageSymbolConfiguration = _Class("UIImageSymbolConfiguration")
_UIImageSymbolConfiguration = _Class("_UIImageSymbolConfiguration")
_UICalloutBarSystemButtonDescription = _Class("_UICalloutBarSystemButtonDescription")
_UIViewVisitor = _Class("_UIViewVisitor")
_UIAccessibilityInterfaceStyleVisitor = _Class("_UIAccessibilityInterfaceStyleVisitor")
_UIFocusTrackingVisitor = _Class("_UIFocusTrackingVisitor")
_UIMotionEffectsVisitor = _Class("_UIMotionEffectsVisitor")
_UIViewBlockVisitor = _Class("_UIViewBlockVisitor")
_UITintColorVisitor = _Class("_UITintColorVisitor")
UIColor = _Class("UIColor")
UICIColor = _Class("UICIColor")
UIDisplayP3Color = _Class("UIDisplayP3Color")
NSColor = _Class("NSColor")
UICGColor = _Class("UICGColor")
UIPatternCGColor = _Class("UIPatternCGColor")
UICachedPatternCGColor = _Class("UICachedPatternCGColor")
UIDeviceRGBColor = _Class("UIDeviceRGBColor")
UICachedDeviceRGBColor = _Class("UICachedDeviceRGBColor")
UIDynamicColor = _Class("UIDynamicColor")
UIDynamicPatternColor = _Class("UIDynamicPatternColor")
UIDynamicAppDefinedColor = _Class("UIDynamicAppDefinedColor")
UIDynamicProviderColor = _Class("UIDynamicProviderColor")
UIDynamicCatalogColor = _Class("UIDynamicCatalogColor")
UIDynamicModifiedColor = _Class("UIDynamicModifiedColor")
UIDynamicSystemColor = _Class("UIDynamicSystemColor")
UIDeviceWhiteColor = _Class("UIDeviceWhiteColor")
UICachedDeviceWhiteColor = _Class("UICachedDeviceWhiteColor")
UIPlaceholderColor = _Class("UIPlaceholderColor")
_UIVisualEffectViewCornerMask = _Class("_UIVisualEffectViewCornerMask")
_UIVisualEffectFilterEntry = _Class("_UIVisualEffectFilterEntry")
_UIVisualEffectDescriptor = _Class("_UIVisualEffectDescriptor")
_UIVisualEffectHost = _Class("_UIVisualEffectHost")
_UIBlurEffectImpl = _Class("_UIBlurEffectImpl")
_UIBlurEffectCoreUIImpl = _Class("_UIBlurEffectCoreUIImpl")
_UIBlurEffectLegacyImpl = _Class("_UIBlurEffectLegacyImpl")
_UIBlurEffectModernImpl = _Class("_UIBlurEffectModernImpl")
_UIBlurEffectCoreMaterialImpl = _Class("_UIBlurEffectCoreMaterialImpl")
_UIBlurEffectAverageImpl = _Class("_UIBlurEffectAverageImpl")
UIVisualEffect = _Class("UIVisualEffect")
_UIWallpaperEffect = _Class("_UIWallpaperEffect")
_UICopyEffect = _Class("_UICopyEffect")
_UIOverlayEffect = _Class("_UIOverlayEffect")
_UIZoomEffect = _Class("_UIZoomEffect")
_UICompoundEffect = _Class("_UICompoundEffect")
_UIEmptyEffect = _Class("_UIEmptyEffect")
UIVibrancyEffect = _Class("UIVibrancyEffect")
UIColorEffect = _Class("UIColorEffect")
UIBlurEffect = _Class("UIBlurEffect")
_UIPopoverBackgroundVisualEffect = _Class("_UIPopoverBackgroundVisualEffect")
_UICoreUIEffect = _Class("_UICoreUIEffect")
_UIBlurThroughEffect = _Class("_UIBlurThroughEffect")
_UINoBlurEffect = _Class("_UINoBlurEffect")
_UICustomBlurEffect = _Class("_UICustomBlurEffect")
_UIVisualEffectViewBackdropCaptureGroup = _Class(
    "_UIVisualEffectViewBackdropCaptureGroup"
)
_UIVisualEffectEnvironment = _Class("_UIVisualEffectEnvironment")
_UIViewLayoutFeedbackLoopDebugger = _Class("_UIViewLayoutFeedbackLoopDebugger")
UIMenuItem = _Class("UIMenuItem")
UIMenuController = _Class("UIMenuController")
_UIAppearance = _Class("_UIAppearance")
_UIBarItemAppearance = _Class("_UIBarItemAppearance")
_UIPropertyBasedAppearance = _Class("_UIPropertyBasedAppearance")
_UITraitBasedAppearance = _Class("_UITraitBasedAppearance")
_UIViewServiceSessionManager = _Class("_UIViewServiceSessionManager")
_UICanvasUserActivityManager = _Class("_UICanvasUserActivityManager")
_UIAssertionController = _Class("_UIAssertionController")
_UIRemoteKeyboardsEventObserver = _Class("_UIRemoteKeyboardsEventObserver")
_UIObjectPerScreen = _Class("_UIObjectPerScreen")
UIDevice = _Class("UIDevice")
UITraitCollection = _Class("UITraitCollection")
UIApplicationSceneHostAgent = _Class("UIApplicationSceneHostAgent")
UIApplicationSceneClientAgent = _Class("UIApplicationSceneClientAgent")
_UIInterprocessKeyedArchiver = _Class("_UIInterprocessKeyedArchiver")
UIStateRestorationKeyedArchiver = _Class("UIStateRestorationKeyedArchiver")
UIStateRestorationKeyedUnarchiver = _Class("UIStateRestorationKeyedUnarchiver")
UIMutableApplicationSceneClientSettings = _Class(
    "UIMutableApplicationSceneClientSettings"
)
UIApplicationSceneClientSettings = _Class("UIApplicationSceneClientSettings")
UIMutableApplicationSceneSettings = _Class("UIMutableApplicationSceneSettings")
UIMutableCarPlayApplicationSceneSettings = _Class(
    "UIMutableCarPlayApplicationSceneSettings"
)
UIApplicationSceneSettings = _Class("UIApplicationSceneSettings")
UICarPlayApplicationSceneSettings = _Class("UICarPlayApplicationSceneSettings")
UIWindowSceneSpecification = _Class("UIWindowSceneSpecification")
UIApplicationSceneSpecification = _Class("UIApplicationSceneSpecification")
UIApplicationCoverSheetSceneSpecification = _Class(
    "UIApplicationCoverSheetSceneSpecification"
)
UIApplicationStarkSceneSpecification = _Class("UIApplicationStarkSceneSpecification")
UIApplicationExternalScreenSceneSpecification = _Class(
    "UIApplicationExternalScreenSceneSpecification"
)
_UIPopoverSceneSpecification = _Class("_UIPopoverSceneSpecification")
_UIScreenFrameSpecification = _Class("_UIScreenFrameSpecification")
UIScreen = _Class("UIScreen")
_UISceneLifecycleMultiplexer = _Class("_UISceneLifecycleMultiplexer")
_UIRemoteKeyboards = _Class("_UIRemoteKeyboards")
UIInputResponderController = _Class("UIInputResponderController")
UISceneRequestOptions = _Class("UISceneRequestOptions")
UIStatusBarTapAction = _Class("UIStatusBarTapAction")
UIApplicationLegacyVOIPKeepAliveAction = _Class(
    "UIApplicationLegacyVOIPKeepAliveAction"
)
UIPPTRequestAction = _Class("UIPPTRequestAction")
UIStatusBarHoverRegionAction = _Class("UIStatusBarHoverRegionAction")
UIResetFocusAction = _Class("UIResetFocusAction")
UIUnhandledMenuButtonAction = _Class("UIUnhandledMenuButtonAction")
UIUnhandledBackButtonAction = _Class("UIUnhandledBackButtonAction")
UIDismissSceneAction = _Class("UIDismissSceneAction")
UIWillPresentNotificationAction = _Class("UIWillPresentNotificationAction")
UIWatchKitExtensionRequestAction = _Class("UIWatchKitExtensionRequestAction")
UISystemNavigationAction = _Class("UISystemNavigationAction")
UISiriTaskAction = _Class("UISiriTaskAction")
UIScreenshotMetadataRequestAction = _Class("UIScreenshotMetadataRequestAction")
UISceneProposalAction = _Class("UISceneProposalAction")
UISceneHitTestAction = _Class("UISceneHitTestAction")
UIOpenURLAction = _Class("UIOpenURLAction")
UINotificationSettingsAction = _Class("UINotificationSettingsAction")
UINotificationResponseAction = _Class("UINotificationResponseAction")
UIHealthAuthorizationAction = _Class("UIHealthAuthorizationAction")
UIHandleStatusBarTapAction = _Class("UIHandleStatusBarTapAction")
UIHandleLocalNotificationAction = _Class("UIHandleLocalNotificationAction")
UIHandleCloudKitShareAction = _Class("UIHandleCloudKitShareAction")
UIHandleBackgroundURLSessionAction = _Class("UIHandleBackgroundURLSessionAction")
UIHandleApplicationShortcutAction = _Class("UIHandleApplicationShortcutAction")
UIDidTakeScreenshotAction = _Class("UIDidTakeScreenshotAction")
UIBannerAction = _Class("UIBannerAction")
UIActivityContinuationAction = _Class("UIActivityContinuationAction")
UIAccessoryBackgroundTaskAction = _Class("UIAccessoryBackgroundTaskAction")
UIDestroySceneAction = _Class("UIDestroySceneAction")
UIFetchContentInBackgroundAction = _Class("UIFetchContentInBackgroundAction")
UIIntentForwardingAction = _Class("UIIntentForwardingAction")
UIHandleRemoteNotificationAction = _Class("UIHandleRemoteNotificationAction")
UIFocusMovementAction = _Class("UIFocusMovementAction")
UIApplicationSceneTransitionContext = _Class("UIApplicationSceneTransitionContext")
_UIAfterCACommitQueue = _Class("_UIAfterCACommitQueue")
_UISceneEventResponder = _Class("_UISceneEventResponder")
UIContentSizeCategoryPreference = _Class("UIContentSizeCategoryPreference")
_UIContentSizeCategoryPreferenceSystem = _Class(
    "_UIContentSizeCategoryPreferenceSystem"
)
_UIApplicationInfoParser = _Class("_UIApplicationInfoParser")
UIActivityContinuationManager = _Class("UIActivityContinuationManager")
UIEvent = _Class("UIEvent")
_UIGameControllerEvent = _Class("_UIGameControllerEvent")
UIMoveEvent = _Class("UIMoveEvent")
UITransformEvent = _Class("UITransformEvent")
UIDragEvent = _Class("UIDragEvent")
UIScrollEvent = _Class("UIScrollEvent")
UIHoverEvent = _Class("UIHoverEvent")
UITouchesEvent = _Class("UITouchesEvent")
UIPencilEvent = _Class("UIPencilEvent")
UIMotionEvent = _Class("UIMotionEvent")
UIRemoteControlEvent = _Class("UIRemoteControlEvent")
UIWheelEvent = _Class("UIWheelEvent")
UIPressesEvent = _Class("UIPressesEvent")
UIPhysicalKeyboardEvent = _Class("UIPhysicalKeyboardEvent")
UIEventEnvironment = _Class("UIEventEnvironment")
UIEventDispatcher = _Class("UIEventDispatcher")
UIGestureGraph = _Class("UIGestureGraph")
UIGestureEnvironment = _Class("UIGestureEnvironment")
_UIHIDTransformer = _Class("_UIHIDTransformer")
UIEventFetcher = _Class("UIEventFetcher")
_UIDeviceInitialDeviceConfigurationLoader = _Class(
    "_UIDeviceInitialDeviceConfigurationLoader"
)
_UIScreenInitialDisplayConfigurationLoader = _Class(
    "_UIScreenInitialDisplayConfigurationLoader"
)
_UIApplicationConfigurationLoader = _Class("_UIApplicationConfigurationLoader")
UIWebLayer = _Class("UIWebLayer")
_UIWebDocumentViewRotationLayer = _Class("_UIWebDocumentViewRotationLayer")
_UIStackedImageContainerLayer = _Class("_UIStackedImageContainerLayer")
_UIDirectionalRotationLayer = _Class("_UIDirectionalRotationLayer")
_UILabelContentLayer = _Class("_UILabelContentLayer")
_UIVectorLabelLayer = _Class("_UIVectorLabelLayer")
_UIContentViewAnimationStateUpdatingLayer = _Class(
    "_UIContentViewAnimationStateUpdatingLayer"
)
_UIReplicantLayer = _Class("_UIReplicantLayer")
_UICircleProgressLayer = _Class("_UICircleProgressLayer")
_UIBackdropViewLayer = _Class("_UIBackdropViewLayer")
_UIKBKeyViewLayer = _Class("_UIKBKeyViewLayer")
_UITileLayer = _Class("_UITileLayer")
UIFocusRingLayer = _Class("UIFocusRingLayer")
UIFocusRingDefaultShapeLayer = _Class("UIFocusRingDefaultShapeLayer")
_UITextTiledLayer = _Class("_UITextTiledLayer")
UIWindowLayer = _Class("UIWindowLayer")
_UIWindowTransformLayer = _Class("_UIWindowTransformLayer")
_UILabelLayer = _Class("_UILabelLayer")
UICABackdropLayer = _Class("UICABackdropLayer")
_UIFlippingLayer = _Class("_UIFlippingLayer")
UIWebPDFSearchOperation = _Class("UIWebPDFSearchOperation")
_UIDocumentActivityDownloadOperation = _Class("_UIDocumentActivityDownloadOperation")
UIDictationStreamingOperation = _Class("UIDictationStreamingOperation")
UIKBTreeLocalizedKeylistEnumerator = _Class("UIKBTreeLocalizedKeylistEnumerator")
_UIGetAssetThread = _Class("_UIGetAssetThread")
WebPDFNSNumberFormatter = _Class("WebPDFNSNumberFormatter")
_UICascadingTextStorage = _Class("_UICascadingTextStorage")
_UIDatePickerChineseCalendar = _Class("_UIDatePickerChineseCalendar")
UIResponder = _Class("UIResponder")
_UITextServicesResponderProxy = _Class("_UITextServicesResponderProxy")
_UIKeyboardHandwritingLink = _Class("_UIKeyboardHandwritingLink")
_UITextLoupeResponderProxy = _Class("_UITextLoupeResponderProxy")
UIApplication = _Class("UIApplication")
UISystemShellApplication = _Class("UISystemShellApplication")
UITextInteractionSelectableInputDelegate = _Class(
    "UITextInteractionSelectableInputDelegate"
)
UIScene = _Class("UIScene")
UIWindowScene = _Class("UIWindowScene")
_UIPopoverScene = _Class("_UIPopoverScene")
_UIScreenBasedWindowScene = _Class("_UIScreenBasedWindowScene")
_UIKeyboardWindowScene = _Class("_UIKeyboardWindowScene")
_UIPlaceholderWindowScene = _Class("_UIPlaceholderWindowScene")
UICanvas = _Class("UICanvas")
_UICanvas = _Class("_UICanvas")
UIAccessibilityElement = _Class("UIAccessibilityElement")
UIView = _Class("UIView")
_UITouchFallbackView = _Class("_UITouchFallbackView")
_UIShareInvitationRemoteViewControllerTintColorView = _Class(
    "_UIShareInvitationRemoteViewControllerTintColorView"
)
_UIAttributedStringView = _Class("_UIAttributedStringView")
_UIWebFindOnPageHighlightBubbleView = _Class("_UIWebFindOnPageHighlightBubbleView")
_UIStackedImageContainerView = _Class("_UIStackedImageContainerView")
_UIStackedImageLayerWrappingView = _Class("_UIStackedImageLayerWrappingView")
_UIStackedImageLayerDelegate = _Class("_UIStackedImageLayerDelegate")
_UIPlatterContainerView = _Class("_UIPlatterContainerView")
_UIPopoverViewBackgroundComponentView = _Class("_UIPopoverViewBackgroundComponentView")
_UIMirrorNinePatchView = _Class("_UIMirrorNinePatchView")
_UIGlintyStringView = _Class("_UIGlintyStringView")
_UIGlintyGradientView = _Class("_UIGlintyGradientView")
_UIGlintyShapeView = _Class("_UIGlintyShapeView")
_UIExpandingGlyphsView = _Class("_UIExpandingGlyphsView")
_UIContentUnavailableView = _Class("_UIContentUnavailableView")
_UIContentUnavailableViewTV = _Class("_UIContentUnavailableViewTV")
_UICircleProgressIndicator = _Class("_UICircleProgressIndicator")
_UICAPackageView = _Class("_UICAPackageView")
_UIAccessDeniedView = _Class("_UIAccessDeniedView")
_UIReflectingView = _Class("_UIReflectingView")
_UIReflectingGradientView = _Class("_UIReflectingGradientView")
_UIReflectingContainerView = _Class("_UIReflectingContainerView")
_UIImageViewOverlayView = _Class("_UIImageViewOverlayView")
_UIStaticScrollBar = _Class("_UIStaticScrollBar")
_UIDatePickerCalendarHeaderView = _Class("_UIDatePickerCalendarHeaderView")
_UIBasicCellContentView = _Class("_UIBasicCellContentView")
_UIDebugAlignmentRectView = _Class("_UIDebugAlignmentRectView")
_UIDatePickerCalendarMonthYearSelector = _Class(
    "_UIDatePickerCalendarMonthYearSelector"
)
_UIDebugColorBoundsView = _Class("_UIDebugColorBoundsView")
_UIPointerEffectPlatterView = _Class("_UIPointerEffectPlatterView")
_UIAnimatedAttachmentView = _Class("_UIAnimatedAttachmentView")
_UIDragDestinationIndicatorView = _Class("_UIDragDestinationIndicatorView")
_UIMorphingView = _Class("_UIMorphingView")
_UIDynamicCaretAlternatives = _Class("_UIDynamicCaretAlternatives")
_UIDynamicCaretInput = _Class("_UIDynamicCaretInput")
_UIDynamicCaretDot = _Class("_UIDynamicCaretDot")
_UIPageControlIndicatorContentView = _Class("_UIPageControlIndicatorContentView")
_UIPageControlContentView = _Class("_UIPageControlContentView")
_UITextDragCaretView = _Class("_UITextDragCaretView")
_UITableViewSeparatorView = _Class("_UITableViewSeparatorView")
_UITableViewHeaderFooterContentView = _Class("_UITableViewHeaderFooterContentView")
_UITableViewHeaderFooterViewBackground = _Class(
    "_UITableViewHeaderFooterViewBackground"
)
_UIFocusLinearMovementDebugView = _Class("_UIFocusLinearMovementDebugView")
_UIClickHighlightInteractionEffectAnchorView = _Class(
    "_UIClickHighlightInteractionEffectAnchorView"
)
_UITableViewCellBadge = _Class("_UITableViewCellBadge")
_UITableViewCellVerticalSeparator = _Class("_UITableViewCellVerticalSeparator")
_UIStatusBarLocalView = _Class("_UIStatusBarLocalView")
_UIStatusBar = _Class("_UIStatusBar")
_UIStatusBarForegroundView = _Class("_UIStatusBarForegroundView")
_UIStatusBarMultilineStringView = _Class("_UIStatusBarMultilineStringView")
_UIStatusBarLockView = _Class("_UIStatusBarLockView")
_UIStatusBarDualCellularSignalView = _Class("_UIStatusBarDualCellularSignalView")
_UIStatusBarBadgeView = _Class("_UIStatusBarBadgeView")
_UIStatusBarActivityView = _Class("_UIStatusBarActivityView")
_UIHighlightPlatterView = _Class("_UIHighlightPlatterView")
_UIAnchoredClickHighlightPlatterView = _Class("_UIAnchoredClickHighlightPlatterView")
_UIStatusBarLockItemPadlockView = _Class("_UIStatusBarLockItemPadlockView")
_UIBannerView = _Class("_UIBannerView")
_UIBannerContainerView = _Class("_UIBannerContainerView")
_UIReplicantView = _Class("_UIReplicantView")
_UISearchControllerLimitedAccessView = _Class("_UISearchControllerLimitedAccessView")
_UISearchControllerTVKeyboardContainerView = _Class(
    "_UISearchControllerTVKeyboardContainerView"
)
_UISearchControllerView = _Class("_UISearchControllerView")
_UISearchAtomBackgroundView = _Class("_UISearchAtomBackgroundView")
_UISearchAtomView = _Class("_UISearchAtomView")
_UIPrintMessageAndSpinnerView = _Class("_UIPrintMessageAndSpinnerView")
_UIPlatterTransformView = _Class("_UIPlatterTransformView")
_UIPreviewPlatterView = _Class("_UIPreviewPlatterView")
_UIPlatterClippingView = _Class("_UIPlatterClippingView")
_UIOnePartImageView = _Class("_UIOnePartImageView")
_UIPickerViewTopFrame = _Class("_UIPickerViewTopFrame")
_UIPreviewPresentationContainerView = _Class("_UIPreviewPresentationContainerView")
_UIPreviewPresentationPlatterView = _Class("_UIPreviewPresentationPlatterView")
_UIPreviewPresentationEffectView = _Class("_UIPreviewPresentationEffectView")
_UIPortalView = _Class("_UIPortalView")
_UIInteractiveHighlightContentView = _Class("_UIInteractiveHighlightContentView")
_UIPreviewQuickActionView = _Class("_UIPreviewQuickActionView")
_UIPreviewActionSheetView = _Class("_UIPreviewActionSheetView")
_UIPreviewActionSheetTitleView = _Class("_UIPreviewActionSheetTitleView")
_UIPreviewActionSheetItemView = _Class("_UIPreviewActionSheetItemView")
_UIContextMenuReparentingContainerView = _Class(
    "_UIContextMenuReparentingContainerView"
)
_UIValueCellContentView = _Class("_UIValueCellContentView")
_UISlideriOSVisualElement = _Class("_UISlideriOSVisualElement")
_UISubtitleCellContentView = _Class("_UISubtitleCellContentView")
_UIKBRTFingerDetectionFingerFeedbackView = _Class(
    "_UIKBRTFingerDetectionFingerFeedbackView"
)
_UIKBRTFingerDetectionFingerCircleView = _Class(
    "_UIKBRTFingerDetectionFingerCircleView"
)
_UIKBRTFingerDetectionView = _Class("_UIKBRTFingerDetectionView")
_UIKBRTTouchDrifingFingerCircleView = _Class("_UIKBRTTouchDrifingFingerCircleView")
_UITextFieldSystemBackgroundView = _Class("_UITextFieldSystemBackgroundView")
_UIKeyboardPopoverAffordance = _Class("_UIKeyboardPopoverAffordance")
_UIKeyboardPopover = _Class("_UIKeyboardPopover")
_UICollectionViewLayoutSwipeMaskView = _Class("_UICollectionViewLayoutSwipeMaskView")
_UIContextMenuAccessoryView = _Class("_UIContextMenuAccessoryView")
_UIKBCompositeImageView = _Class("_UIKBCompositeImageView")
_UIContextMenuActionView = _Class("_UIContextMenuActionView")
_UIContextMenuLoadingActionView = _Class("_UIContextMenuLoadingActionView")
_UIConstraintBasedLayoutHostingView = _Class("_UIConstraintBasedLayoutHostingView")
_UIRadiosityShadowView = _Class("_UIRadiosityShadowView")
_UIStatusBarSensorActivityView = _Class("_UIStatusBarSensorActivityView")
_UIRecentsAccessoryDefaultView = _Class("_UIRecentsAccessoryDefaultView")
_UILumaTrackingBackdropView = _Class("_UILumaTrackingBackdropView")
_UISearchBarCompatibilityClippingView = _Class("_UISearchBarCompatibilityClippingView")
_UIKeyboardCandidateSlidingMaskView = _Class("_UIKeyboardCandidateSlidingMaskView")
_UIKeyboardCandidateSnapshotView = _Class("_UIKeyboardCandidateSnapshotView")
_UICollectionViewListAccessoryVerticalSeparator = _Class(
    "_UICollectionViewListAccessoryVerticalSeparator"
)
_UIDatePickerCalendarDateView = _Class("_UIDatePickerCalendarDateView")
_UILegibilityView = _Class("_UILegibilityView")
_UILegibilityLabel = _Class("_UILegibilityLabel")
_UIStatusBarVPNDisconnectView = _Class("_UIStatusBarVPNDisconnectView")
_UIHighlightView = _Class("_UIHighlightView")
_UISceneSnapshotPresentationView = _Class("_UISceneSnapshotPresentationView")
_UISceneLayerHostContainerView = _Class("_UISceneLayerHostContainerView")
_UIBatteryView = _Class("_UIBatteryView")
_UIStaticBatteryView = _Class("_UIStaticBatteryView")
_CarTitleView = _Class("_CarTitleView")
_UIFocusFastScrollingIndexBarView = _Class("_UIFocusFastScrollingIndexBarView")
_UIFocusFastScrollingIndexBarIndicatorView = _Class(
    "_UIFocusFastScrollingIndexBarIndicatorView"
)
_UIHorizontalIndexTitleBar = _Class("_UIHorizontalIndexTitleBar")
_UIFieldEditorSystemInputHostView = _Class("_UIFieldEditorSystemInputHostView")
_UIDatePickerLinkedLabel = _Class("_UIDatePickerLinkedLabel")
_UIDragBadge = _Class("_UIDragBadge")
_UIShapeView = _Class("_UIShapeView")
_UIPlatterView = _Class("_UIPlatterView")
_UIPlatterShadowView = _Class("_UIPlatterShadowView")
_UIGradientView = _Class("_UIGradientView")
_UIDocumentPickerRemoteViewControllerTintColorView = _Class(
    "_UIDocumentPickerRemoteViewControllerTintColorView"
)
_UIActionSliderTrackComponentView = _Class("_UIActionSliderTrackComponentView")
_UIActionSliderKnob = _Class("_UIActionSliderKnob")
_UIButtonMaskAnimationView = _Class("_UIButtonMaskAnimationView")
_UIButtonContentCenteringSpacer = _Class("_UIButtonContentCenteringSpacer")
_UIProgressView = _Class("_UIProgressView")
_UICircleProgressView = _Class("_UICircleProgressView")
_UIDatePickerCalendarTimeView = _Class("_UIDatePickerCalendarTimeView")
_UIFlippingView = _Class("_UIFlippingView")
_UIPanelControllerMeshAnimatingTransitionView = _Class(
    "_UIPanelControllerMeshAnimatingTransitionView"
)
_UIShortDefinitionView = _Class("_UIShortDefinitionView")
_UIPageViewControllerContentView = _Class("_UIPageViewControllerContentView")
_UINavigationControllerPaletteClippingView = _Class(
    "_UINavigationControllerPaletteClippingView"
)
_UIPPPCDebugDot = _Class("_UIPPPCDebugDot")
_UICollectionViewMaskView = _Class("_UICollectionViewMaskView")
_UIContextMenuCommitContainerView = _Class("_UIContextMenuCommitContainerView")
_UICollectionViewListCellBackgroundView = _Class(
    "_UICollectionViewListCellBackgroundView"
)
_UICollectionViewListCellSelectedBackgroundView = _Class(
    "_UICollectionViewListCellSelectedBackgroundView"
)
_UIDirectionalRotationView = _Class("_UIDirectionalRotationView")
_UISceneLayerHostView = _Class("_UISceneLayerHostView")
_UIExternalSceneLayerHostView = _Class("_UIExternalSceneLayerHostView")
_UIContextLayerHostView = _Class("_UIContextLayerHostView")
_UIKeyboardLayerHostView = _Class("_UIKeyboardLayerHostView")
_UISystemBackgroundStrokeView = _Class("_UISystemBackgroundStrokeView")
_UINavigationControllerPalette = _Class("_UINavigationControllerPalette")
_UINavigationControllerManagedSearchPalette = _Class(
    "_UINavigationControllerManagedSearchPalette"
)
_UIBadgeView = _Class("_UIBadgeView")
_UISearchTokenLayoutView = _Class("_UISearchTokenLayoutView")
_UIContextMenuContainerView = _Class("_UIContextMenuContainerView")
_UISearchBarScopeContainerView = _Class("_UISearchBarScopeContainerView")
_UISearchBarPromptContainerView = _Class("_UISearchBarPromptContainerView")
_UISearchBarContainerView = _Class("_UISearchBarContainerView")
_UIColorWellConicalGradientBackgroundView = _Class(
    "_UIColorWellConicalGradientBackgroundView"
)
_UINavigationBarPalette = _Class("_UINavigationBarPalette")
_UINavigationBarLegacyContentView = _Class("_UINavigationBarLegacyContentView")
_UINavBarPrompt = _Class("_UINavBarPrompt")
_UINavigationBarTitleView = _Class("_UINavigationBarTitleView")
_UIBarBackgroundTopCurtainView = _Class("_UIBarBackgroundTopCurtainView")
_UIGroupedBar = _Class("_UIGroupedBar")
_UIUCBKBSelectionBackground = _Class("_UIUCBKBSelectionBackground")
_UIFloatingShadowView = _Class("_UIFloatingShadowView")
_UIFloatingContentView = _Class("_UIFloatingContentView")
_UIKBFloatingContentView = _Class("_UIKBFloatingContentView")
_UIFloatingContentCornerRadiusAnimatingView = _Class(
    "_UIFloatingContentCornerRadiusAnimatingView"
)
_UIFloatingContentCornerRadiusAnimatingScreenScaleInheritingView = _Class(
    "_UIFloatingContentCornerRadiusAnimatingScreenScaleInheritingView"
)
_UIFloatingContentTransformView = _Class("_UIFloatingContentTransformView")
_UIBasicHeaderFooterContentView = _Class("_UIBasicHeaderFooterContentView")
_UIBackdropContentView = _Class("_UIBackdropContentView")
_UIBackdropEffectView = _Class("_UIBackdropEffectView")
_UIStatusBarPersistentAnimationView = _Class("_UIStatusBarPersistentAnimationView")
_UIStatusBarSignalView = _Class("_UIStatusBarSignalView")
_UIStatusBarWifiSignalView = _Class("_UIStatusBarWifiSignalView")
_UIStatusBarCellularSignalView = _Class("_UIStatusBarCellularSignalView")
_UIStatusBarCellularSmallSignalView = _Class("_UIStatusBarCellularSmallSignalView")
_UIStatusBarCellularFlatSignalView = _Class("_UIStatusBarCellularFlatSignalView")
_UIStatusBarRoundedCornerView = _Class("_UIStatusBarRoundedCornerView")
_UIStatusBarPillView = _Class("_UIStatusBarPillView")
_UIDatePickerCalendarView = _Class("_UIDatePickerCalendarView")
_UIAlertControllerTVBackgroundView = _Class("_UIAlertControllerTVBackgroundView")
_UIAlertControllerCarBackgroundView = _Class("_UIAlertControllerCarBackgroundView")
_UIAlertControllerCarActionHighlightedBackgroundView = _Class(
    "_UIAlertControllerCarActionHighlightedBackgroundView"
)
_UIDatePickerCalendarTimeLabel = _Class("_UIDatePickerCalendarTimeLabel")
_UIAlertControllerGradientView = _Class("_UIAlertControllerGradientView")
_UIContextMenuActionsListView = _Class("_UIContextMenuActionsListView")
_UIAlertControllerTextFieldView = _Class("_UIAlertControllerTextFieldView")
_UIInterfaceActionBlankSeparatorView = _Class("_UIInterfaceActionBlankSeparatorView")
_UIInterfaceActionVibrantBorderView = _Class("_UIInterfaceActionVibrantBorderView")
_UIBlendingHighlightView = _Class("_UIBlendingHighlightView")
_UIInterfaceActionBlendingSeparatorView = _Class(
    "_UIInterfaceActionBlendingSeparatorView"
)
_UIInterfaceActionBlendingBorderView = _Class("_UIInterfaceActionBlendingBorderView")
_UIInterfaceActionLabelsPropertyView = _Class("_UIInterfaceActionLabelsPropertyView")
_UITabBarAccessoryView = _Class("_UITabBarAccessoryView")
_UIPlatterSoftShadowView = _Class("_UIPlatterSoftShadowView")
_UIAlertControlleriOSHighlightedBackgroundView = _Class(
    "_UIAlertControlleriOSHighlightedBackgroundView"
)
_UIInterfaceActionVibrantSeparatorView = _Class(
    "_UIInterfaceActionVibrantSeparatorView"
)
_UIAlertControllerActionView = _Class("_UIAlertControllerActionView")
_UIDimmingKnockoutBackdropView = _Class("_UIDimmingKnockoutBackdropView")
_UIInterfaceActionSeparatableSequenceView = _Class(
    "_UIInterfaceActionSeparatableSequenceView"
)
_UIAlertControllerView = _Class("_UIAlertControllerView")
_UIKeyboardLayoutAlignmentView = _Class("_UIKeyboardLayoutAlignmentView")
_UIBackButtonMaskView = _Class("_UIBackButtonMaskView")
_UIParallaxDimmingView = _Class("_UIParallaxDimmingView")
_UITableViewCellSeparatorView = _Class("_UITableViewCellSeparatorView")
_UIRefreshControlModernReplicatorView = _Class("_UIRefreshControlModernReplicatorView")
_UIRefreshControlContentView = _Class("_UIRefreshControlContentView")
_UIRefreshControlModernContentView = _Class("_UIRefreshControlModernContentView")
_UIKBCompatInputView = _Class("_UIKBCompatInputView")
_UIGroupTableViewCellBackground_TV = _Class("_UIGroupTableViewCellBackground_TV")
_UIScrollViewGradientMaskView = _Class("_UIScrollViewGradientMaskView")
_UIBackdropView = _Class("_UIBackdropView")
_UISystemBackgroundView = _Class("_UISystemBackgroundView")
_UITAMICAdaptorView = _Class("_UITAMICAdaptorView")
_UIScrollViewScrollIndicator = _Class("_UIScrollViewScrollIndicator")
_UINavigationItemView = _Class("_UINavigationItemView")
_UINavigationItemButtonView = _Class("_UINavigationItemButtonView")
_UITableViewContainerView = _Class("_UITableViewContainerView")
_UITableViewDropAnimationContainerView = _Class(
    "_UITableViewDropAnimationContainerView"
)
_UITableViewCellSwipeContainerView = _Class("_UITableViewCellSwipeContainerView")
_UIInputViewContent = _Class("_UIInputViewContent")
_UITextLayoutView = _Class("_UITextLayoutView")
_UILayoutGuide = _Class("_UILayoutGuide")
_UIPanelControllerContentView = _Class("_UIPanelControllerContentView")
_UINavigationBarModernPromptView = _Class("_UINavigationBarModernPromptView")
_UINavigationBarLargeTitleView = _Class("_UINavigationBarLargeTitleView")
_UIBarContentView = _Class("_UIBarContentView")
_UIToolbarContentView = _Class("_UIToolbarContentView")
_UINavigationBarContentView = _Class("_UINavigationBarContentView")
_UIBarBackground = _Class("_UIBarBackground")
_UIRemoteKeyboardPlaceholderView = _Class("_UIRemoteKeyboardPlaceholderView")
_UISizeTrackingView = _Class("_UISizeTrackingView")
_UIVisibilityPropagationView = _Class("_UIVisibilityPropagationView")
_UIScenePresentationView = _Class("_UIScenePresentationView")
_UILayerHostView = _Class("_UILayerHostView")
_UIRemoteView = _Class("_UIRemoteView")
_UITextEffectsRemoteView = _Class("_UITextEffectsRemoteView")
_UITextFieldRoundedRectBackgroundViewNeue = _Class(
    "_UITextFieldRoundedRectBackgroundViewNeue"
)
_UISearchBarSearchFieldBackgroundView = _Class("_UISearchBarSearchFieldBackgroundView")
_UITextContainerView = _Class("_UITextContainerView")
_UITextCanvasView = _Class("_UITextCanvasView")
_UITextViewCanvasView = _Class("_UITextViewCanvasView")
_UITextFieldCanvasView = _Class("_UITextFieldCanvasView")
_UISearchTextFieldCanvasView = _Class("_UISearchTextFieldCanvasView")
_UISearchBarSearchContainerView = _Class("_UISearchBarSearchContainerView")
_UIPopoverView = _Class("_UIPopoverView")
_UIViewServiceDummyPopoverView = _Class("_UIViewServiceDummyPopoverView")
_UIVisualEffectSubview = _Class("_UIVisualEffectSubview")
_UIVisualEffectContentView = _Class("_UIVisualEffectContentView")
_UIVisualEffectBackdropView = _Class("_UIVisualEffectBackdropView")
UIWebPDFLabelView = _Class("UIWebPDFLabelView")
UIWebOverflowContentView = _Class("UIWebOverflowContentView")
UIWebView = _Class("UIWebView")
UIWebPlaybackTargetPicker = _Class("UIWebPlaybackTargetPicker")
UIWebPDFView = _Class("UIWebPDFView")
UIWebTiledView = _Class("UIWebTiledView")
UIWebDocumentView = _Class("UIWebDocumentView")
UIWebBrowserView = _Class("UIWebBrowserView")
UIDocumentPasswordView = _Class("UIDocumentPasswordView")
UIKeyboardEmojiFamilyConfigurationView = _Class(
    "UIKeyboardEmojiFamilyConfigurationView"
)
UITransitionView = _Class("UITransitionView")
UISnapshotView = _Class("UISnapshotView")
UIPopoverBackgroundView = _Class("UIPopoverBackgroundView")
_UIPopoverSlidingChromeView = _Class("_UIPopoverSlidingChromeView")
_UIPopoverStandardChromeView = _Class("_UIPopoverStandardChromeView")
_UIViewServiceDummyPopoverBackgroundView = _Class(
    "_UIViewServiceDummyPopoverBackgroundView"
)
UINavigationTransitionView = _Class("UINavigationTransitionView")
UIDropShadowView = _Class("UIDropShadowView")
UIDimmingView = _Class("UIDimmingView")
_UIPopoverDimmingView = _Class("_UIPopoverDimmingView")
UIKBViewForResponderForwarding = _Class("UIKBViewForResponderForwarding")
UIVectorLabel = _Class("UIVectorLabel")
UIStackView = _Class("UIStackView")
_UIDatePickerCalendarContentStackView = _Class("_UIDatePickerCalendarContentStackView")
_UIButtonBarStackView = _Class("_UIButtonBarStackView")
UIStepperHorizontalVisualElement = _Class("UIStepperHorizontalVisualElement")
UIDebuggingZoomLoupeView = _Class("UIDebuggingZoomLoupeView")
UIDebuggingZoomLineView = _Class("UIDebuggingZoomLineView")
UIDebuggingInformationContainerView = _Class("UIDebuggingInformationContainerView")
UIProgressHUD = _Class("UIProgressHUD")
UIPasscodeField = _Class("UIPasscodeField")
UITextAttachmentView = _Class("UITextAttachmentView")
UITextFieldBackgroundView = _Class("UITextFieldBackgroundView")
_UITextFieldPasscodeCutoutBackground = _Class("_UITextFieldPasscodeCutoutBackground")
UITextFieldBorderView = _Class("UITextFieldBorderView")
UISplitAndMaskView = _Class("UISplitAndMaskView")
UIWebDragDotView = _Class("UIWebDragDotView")
UIWebTextRangeView = _Class("UIWebTextRangeView")
UIWebSelectionOutline = _Class("UIWebSelectionOutline")
UIWebSelectionHandle = _Class("UIWebSelectionHandle")
UIWebSelectionView = _Class("UIWebSelectionView")
UITextSelectionView = _Class("UITextSelectionView")
UITextRangeView = _Class("UITextRangeView")
UISelectionGrabber = _Class("UISelectionGrabber")
UIEditingOverlayGestureView = _Class("UIEditingOverlayGestureView")
UITextMagnifierCommonRenderer = _Class("UITextMagnifierCommonRenderer")
UITextMagnifierRangedRenderer = _Class("UITextMagnifierRangedRenderer")
UITextMagnifierCaretRenderer = _Class("UITextMagnifierCaretRenderer")
UITextMagnifier = _Class("UITextMagnifier")
UITextMagnifierRanged = _Class("UITextMagnifierRanged")
UITextMagnifierCaret = _Class("UITextMagnifierCaret")
UITextContentView = _Class("UITextContentView")
UIURLDragPreviewView = _Class("UIURLDragPreviewView")
UITableViewCellContentMirror = _Class("UITableViewCellContentMirror")
UITableViewHeaderFooterView = _Class("UITableViewHeaderFooterView")
UIShadowView = _Class("UIShadowView")
UITableViewIndexOverlaySelectionView = _Class("UITableViewIndexOverlaySelectionView")
UITableViewIndexOverlayIndicatorView = _Class("UITableViewIndexOverlayIndicatorView")
UITableViewCellContentView = _Class("UITableViewCellContentView")
UITableViewCellSelectedBackground = _Class("UITableViewCellSelectedBackground")
UISwipeActionPullView = _Class("UISwipeActionPullView")
UISwipeActionDeleteScanlineView = _Class("UISwipeActionDeleteScanlineView")
UIListContentView = _Class("UIListContentView")
UIStatusBarForegroundView = _Class("UIStatusBarForegroundView")
UIStatusBarBackgroundView = _Class("UIStatusBarBackgroundView")
_UIScrollsToTopInitiatorView = _Class("_UIScrollsToTopInitiatorView")
UIStatusBar_Base = _Class("UIStatusBar_Base")
UIStatusBar_Placeholder = _Class("UIStatusBar_Placeholder")
UIStatusBar_Modern = _Class("UIStatusBar_Modern")
UIStatusBar = _Class("UIStatusBar")
UIKeyboardKeyplaneSnapshotView = _Class("UIKeyboardKeyplaneSnapshotView")
UIStatusBarItemView = _Class("UIStatusBarItemView")
UIStatusBarDateTimeItemView = _Class("UIStatusBarDateTimeItemView")
UIStatusBarDateItemView = _Class("UIStatusBarDateItemView")
UIStatusBarTimeItemView = _Class("UIStatusBarTimeItemView")
UIStatusBarThermalColorItemView = _Class("UIStatusBarThermalColorItemView")
UIStatusBarTetheringItemView = _Class("UIStatusBarTetheringItemView")
UIStatusBarSignalStrengthItemView = _Class("UIStatusBarSignalStrengthItemView")
UIStatusBarSecondarySignalStrengthItemView = _Class(
    "UIStatusBarSecondarySignalStrengthItemView"
)
UIStatusBarServiceItemView = _Class("UIStatusBarServiceItemView")
UIStatusBarPersonNameItemView = _Class("UIStatusBarPersonNameItemView")
UIStatusBarNotChargingItemView = _Class("UIStatusBarNotChargingItemView")
UIStatusBarLockItemView = _Class("UIStatusBarLockItemView")
UIStatusBarLocationItemView = _Class("UIStatusBarLocationItemView")
UIStatusBarLiquidDetectionItemView = _Class("UIStatusBarLiquidDetectionItemView")
UIStatusBarElectronicTollCollectionItemView = _Class(
    "UIStatusBarElectronicTollCollectionItemView"
)
UIStatusBarDoubleHeightItemView = _Class("UIStatusBarDoubleHeightItemView")
UIStatusBarDataNetworkItemView = _Class("UIStatusBarDataNetworkItemView")
UIStatusBarSecondaryDataNetworkItemView = _Class(
    "UIStatusBarSecondaryDataNetworkItemView"
)
UIStatusBarCarPlayDockItemView = _Class("UIStatusBarCarPlayDockItemView")
UIStatusBarSystemNavigationItemView = _Class("UIStatusBarSystemNavigationItemView")
UIStatusBarOpenInSafariItemView = _Class("UIStatusBarOpenInSafariItemView")
UIStatusBarBreadcrumbItemView = _Class("UIStatusBarBreadcrumbItemView")
UIStatusBarBluetoothItemView = _Class("UIStatusBarBluetoothItemView")
UIStatusBarBluetoothBatteryItemView = _Class("UIStatusBarBluetoothBatteryItemView")
UIStatusBarBatteryPercentItemView = _Class("UIStatusBarBatteryPercentItemView")
UIStatusBarBatteryItemView = _Class("UIStatusBarBatteryItemView")
UIStatusBarButtonActionItemView = _Class("UIStatusBarButtonActionItemView")
UIStatusBarRadarItemView = _Class("UIStatusBarRadarItemView")
UIStatusBarHomeItemView = _Class("UIStatusBarHomeItemView")
UIStatusBarCarPlayTimeItemView = _Class("UIStatusBarCarPlayTimeItemView")
UIStatusBarCarPlayRadarTimeItemView = _Class("UIStatusBarCarPlayRadarTimeItemView")
UIStatusBarCarPlayRecordingTimeItemView = _Class(
    "UIStatusBarCarPlayRecordingTimeItemView"
)
UIStatusBarAppIconItemView = _Class("UIStatusBarAppIconItemView")
UIStatusBarNavigationItemView = _Class("UIStatusBarNavigationItemView")
UIStatusBarReturnToCallItemView = _Class("UIStatusBarReturnToCallItemView")
UIStatusBarIndicatorItemView = _Class("UIStatusBarIndicatorItemView")
UIStatusBarStudentItemView = _Class("UIStatusBarStudentItemView")
UIStatusBarQuietModeItemView = _Class("UIStatusBarQuietModeItemView")
UIStatusBarCarPlayItemView = _Class("UIStatusBarCarPlayItemView")
UIStatusBarAirplaneModeItemView = _Class("UIStatusBarAirplaneModeItemView")
UIStatusBarActivityItemView = _Class("UIStatusBarActivityItemView")
UIKeyCommandDiscoverabilityHUDView = _Class("UIKeyCommandDiscoverabilityHUDView")
UIKeyCommandDiscoverabilityHUDDescriptionView = _Class(
    "UIKeyCommandDiscoverabilityHUDDescriptionView"
)
UIKeyCommandDiscoverabilityHUDColumnView = _Class(
    "UIKeyCommandDiscoverabilityHUDColumnView"
)
UIProgressView = _Class("UIProgressView")
UIActivityIndicatorView = _Class("UIActivityIndicatorView")
_UIStatusBarActivityIndicator = _Class("_UIStatusBarActivityIndicator")
UIProgressIndicator = _Class("UIProgressIndicator")
UIPrintingMessageView = _Class("UIPrintingMessageView")
SupplyLevelView = _Class("SupplyLevelView")
UIPrinterSetupDisplayPINView = _Class("UIPrinterSetupDisplayPINView")
UIPrinterSetupConnectingView = _Class("UIPrinterSetupConnectingView")
UIPrinterSearchingView = _Class("UIPrinterSearchingView")
UIPrinterAccessoryView = _Class("UIPrinterAccessoryView")
UIPickerColumnView = _Class("UIPickerColumnView")
UIDatePickerWeekMonthDayView = _Class("UIDatePickerWeekMonthDayView")
UIDatePickerContentView = _Class("UIDatePickerContentView")
UIKBUndoStateHUD = _Class("UIKBUndoStateHUD")
UIKBUndoInteractionHUD = _Class("UIKBUndoInteractionHUD")
UIKBUndoHUDContainerView = _Class("UIKBUndoHUDContainerView")
UIMorphingLabel = _Class("UIMorphingLabel")
UIKeyboardPathEffectView = _Class("UIKeyboardPathEffectView")
UIKBASPCoverView = _Class("UIKBASPCoverView")
UIKeyboardSplitTransitionView = _Class("UIKeyboardSplitTransitionView")
UIKeyboardSliceTransitionView = _Class("UIKeyboardSliceTransitionView")
UIKeyboardFlipTransitionView = _Class("UIKeyboardFlipTransitionView")
UIAssistantBarRoundedButtonView = _Class("UIAssistantBarRoundedButtonView")
UIKeyboardImpl = _Class("UIKeyboardImpl")
UIKeyboardDockView = _Class("UIKeyboardDockView")
UIKeyboard = _Class("UIKeyboard")
UIKeyboardAutomatic = _Class("UIKeyboardAutomatic")
UIKBInputBackdropView = _Class("UIKBInputBackdropView")
UIInputSetHostView = _Class("UIInputSetHostView")
UIInputSetContainerView = _Class("UIInputSetContainerView")
UIKeyboardEmojiWellView = _Class("UIKeyboardEmojiWellView")
UIDefaultKeyboardInput = _Class("UIDefaultKeyboardInput")
UIKBEmojiSnapshotSizingView = _Class("UIKBEmojiSnapshotSizingView")
UIKeyboardEmojiScrubBarView = _Class("UIKeyboardEmojiScrubBarView")
UIDictationView = _Class("UIDictationView")
UIDictationPopUpView = _Class("UIDictationPopUpView")
UIDictationLayoutView = _Class("UIDictationLayoutView")
UIDictationSplitLayoutView = _Class("UIDictationSplitLayoutView")
UIDictationFloatingView = _Class("UIDictationFloatingView")
UIDictationATVLinearView = _Class("UIDictationATVLinearView")
UIDictationFloatingStarkView = _Class("UIDictationFloatingStarkView")
UIKeyboardDicationBackground = _Class("UIKeyboardDicationBackground")
UIKeyboardDicationBackgroundGradientView = _Class(
    "UIKeyboardDicationBackgroundGradientView"
)
UIDictationLandingView = _Class("UIDictationLandingView")
UIKBStrokeView = _Class("UIKBStrokeView")
UIKBDimmingView = _Class("UIKBDimmingView")
UIKeyboardLayout = _Class("UIKeyboardLayout")
UIKeyboardLayoutDictation = _Class("UIKeyboardLayoutDictation")
UIKeyboardLayoutStar = _Class("UIKeyboardLayoutStar")
UIKeyboardLayoutCursor = _Class("UIKeyboardLayoutCursor")
UIKBSplitImageView = _Class("UIKBSplitImageView")
UIKBBackgroundView = _Class("UIKBBackgroundView")
UIKBKeyplaneView = _Class("UIKBKeyplaneView")
UIKBHandwritingStrokeView = _Class("UIKBHandwritingStrokeView")
UIKBKeyView = _Class("UIKBKeyView")
UIHandwritingAssistantView = _Class("UIHandwritingAssistantView")
UIKBViewBackedKeyView = _Class("UIKBViewBackedKeyView")
UIKeyboardEmojiKeyView = _Class("UIKeyboardEmojiKeyView")
UIKeyboardEmojiSplit = _Class("UIKeyboardEmojiSplit")
UIKeyboardEmojiSplitCategoryPicker = _Class("UIKeyboardEmojiSplitCategoryPicker")
UIKeyboardEmojiCollectionInputView = _Class("UIKeyboardEmojiCollectionInputView")
UIKeyboardEmojiSplitCharacterPicker = _Class("UIKeyboardEmojiSplitCharacterPicker")
UIKeyboardEmojiCategoryBar = _Class("UIKeyboardEmojiCategoryBar")
UIKeyboardEmojiCategoryBar_iPad = _Class("UIKeyboardEmojiCategoryBar_iPad")
UIKeyboardEmojiCategoryBar_iPhone = _Class("UIKeyboardEmojiCategoryBar_iPhone")
UIKBRecentInputsView = _Class("UIKBRecentInputsView")
UIKBHandwritingView = _Class("UIKBHandwritingView")
UIKBDictationDisplayView = _Class("UIKBDictationDisplayView")
UIKBCandidateView = _Class("UIKBCandidateView")
UIKBHandwritingCandidateView = _Class("UIKBHandwritingCandidateView")
UIKBLinearCandidateView = _Class("UIKBLinearCandidateView")
UIKBContainerKeyView = _Class("UIKBContainerKeyView")
UIKBFloatingKeyView = _Class("UIKBFloatingKeyView")
UIKBBlurredKeyView = _Class("UIKBBlurredKeyView")
UIKBFocusVCView = _Class("UIKBFocusVCView")
UIInputSwitcherSelectionExtraView = _Class("UIInputSwitcherSelectionExtraView")
UIInputSwitcherShadowView = _Class("UIInputSwitcherShadowView")
UIKeyboardMenuView = _Class("UIKeyboardMenuView")
UIKeyboardDictationMenu = _Class("UIKeyboardDictationMenu")
UIKeyboardSplitControlMenu = _Class("UIKeyboardSplitControlMenu")
UIInputSwitcherView = _Class("UIInputSwitcherView")
UIInputSwitcherTableCellSegmentView = _Class("UIInputSwitcherTableCellSegmentView")
UIInputSwitcherTableCellBackgroundView = _Class(
    "UIInputSwitcherTableCellBackgroundView"
)
UIKeyboardCandidateInlineFloatingView = _Class("UIKeyboardCandidateInlineFloatingView")
UIAutocorrectInlinePrompt = _Class("UIAutocorrectInlinePrompt")
UIAutocorrectTextView = _Class("UIAutocorrectTextView")
UIAutocorrectShadowView = _Class("UIAutocorrectShadowView")
UIKBAutoFillTestTaggerView = _Class("UIKBAutoFillTestTaggerView")
UISystemGestureView = _Class("UISystemGestureView")
UIApplicationRotationFollowingControllerView = _Class(
    "UIApplicationRotationFollowingControllerView"
)
UICheckeredPatternView = _Class("UICheckeredPatternView")
UIKBTutorialMultipageView = _Class("UIKBTutorialMultipageView")
UIKBTutorialSinglePageView = _Class("UIKBTutorialSinglePageView")
UICalloutBar = _Class("UICalloutBar")
UICalloutBarBackground = _Class("UICalloutBarBackground")
UIAssistantBarSeparatorView = _Class("UIAssistantBarSeparatorView")
UIPickerView = _Class("UIPickerView")
_UIDatePickerView = _Class("_UIDatePickerView")
UIPrintRangePickerView = _Class("UIPrintRangePickerView")
UIWebSelectMultiplePicker = _Class("UIWebSelectMultiplePicker")
UIWebSelectSinglePicker = _Class("UIWebSelectSinglePicker")
UIPickerContentView = _Class("UIPickerContentView")
UIDOMHTMLOptionPickerCell = _Class("UIDOMHTMLOptionPickerCell")
UIDOMHTMLOptGroupCell = _Class("UIDOMHTMLOptGroupCell")
UIInputView = _Class("UIInputView")
UIWebFormAccessory = _Class("UIWebFormAccessory")
UISwitchVisualElement = _Class("UISwitchVisualElement")
UISwitchModernVisualElement = _Class("UISwitchModernVisualElement")
UISwitchCarPlayVisualElement = _Class("UISwitchCarPlayVisualElement")
UIMovieScrubberTrackOverlayView = _Class("UIMovieScrubberTrackOverlayView")
UIMovieScrubberTrackView = _Class("UIMovieScrubberTrackView")
UIMovieScrubberEditingView = _Class("UIMovieScrubberEditingView")
UIViewControllerWrapperView = _Class("UIViewControllerWrapperView")
UIPanelWrapperView = _Class("UIPanelWrapperView")
UIPanelBorderView = _Class("UIPanelBorderView")
UIPanelBorderReplicatingView = _Class("UIPanelBorderReplicatingView")
UISearchDisplayControllerContainerView = _Class(
    "UISearchDisplayControllerContainerView"
)
UILayoutContainerView = _Class("UILayoutContainerView")
_UISplitViewControllerPanelImplView = _Class("_UISplitViewControllerPanelImplView")
UICollectionViewControllerWrapperView = _Class("UICollectionViewControllerWrapperView")
_UIAlertControlleriOSActionSheetCancelBackgroundView = _Class(
    "_UIAlertControlleriOSActionSheetCancelBackgroundView"
)
UIActionSheetiOSDismissActionView = _Class("UIActionSheetiOSDismissActionView")
UIScrollView = _Class("UIScrollView")
_UIQueuingScrollView = _Class("_UIQueuingScrollView")
_UICollectionViewOrthogonalScrollerEmbeddedScrollView = _Class(
    "_UICollectionViewOrthogonalScrollerEmbeddedScrollView"
)
_UIAlertControllerShadowedScrollView = _Class("_UIAlertControllerShadowedScrollView")
_UIInterfaceActionGroupHeaderScrollView = _Class(
    "_UIInterfaceActionGroupHeaderScrollView"
)
_UIInterfaceActionRepresentationsSequenceView = _Class(
    "_UIInterfaceActionRepresentationsSequenceView"
)
UIWebOverflowScrollView = _Class("UIWebOverflowScrollView")
UIWebScrollView = _Class("UIWebScrollView")
_UIWebViewScrollView = _Class("_UIWebViewScrollView")
UIFieldEditor = _Class("UIFieldEditor")
_UISearchBarFieldEditor = _Class("_UISearchBarFieldEditor")
UITableViewWrapperView = _Class("UITableViewWrapperView")
UIPrinterSetupPINScrollView = _Class("UIPrinterSetupPINScrollView")
UITextView = _Class("UITextView")
_UISiriTranscriptTextView = _Class("_UISiriTranscriptTextView")
UIKBASPTextView = _Class("UIKBASPTextView")
UITableView = _Class("UITableView")
_UIMoreListTableView = _Class("_UIMoreListTableView")
UIPickerTableView = _Class("UIPickerTableView")
UIInputSwitcherTableView = _Class("UIInputSwitcherTableView")
UISearchResultsTableView = _Class("UISearchResultsTableView")
UIPageControllerScrollView = _Class("UIPageControllerScrollView")
UICollectionView = _Class("UICollectionView")
UIKeyboardEmojiCollectionView = _Class("UIKeyboardEmojiCollectionView")
UITableViewCell = _Class("UITableViewCell")
_UIPrototypingMenuCell = _Class("_UIPrototypingMenuCell")
_UIPrototypingMenuNumberCell = _Class("_UIPrototypingMenuNumberCell")
_UIPrototypingMenuBoolCell = _Class("_UIPrototypingMenuBoolCell")
UIDebuggingIvarTableViewCell = _Class("UIDebuggingIvarTableViewCell")
UIMainPrinterUtilityCell = _Class("UIMainPrinterUtilityCell")
UIPrinterTableViewCell = _Class("UIPrinterTableViewCell")
UIPickerTableViewCell = _Class("UIPickerTableViewCell")
UIPickerTableViewTitledCell = _Class("UIPickerTableViewTitledCell")
UIPickerTableViewWrapperCell = _Class("UIPickerTableViewWrapperCell")
UIKeyboardEmojiSplitCategoryCell = _Class("UIKeyboardEmojiSplitCategoryCell")
UIRecentInputTableCell = _Class("UIRecentInputTableCell")
UIInputSwitcherTableCell = _Class("UIInputSwitcherTableCell")
UIInputSwitcherSegmentedTableCell = _Class("UIInputSwitcherSegmentedTableCell")
UIExpandedBarItemTableCell = _Class("UIExpandedBarItemTableCell")
UITableViewCollectionCell = _Class("UITableViewCollectionCell")
UICollectionReusableView = _Class("UICollectionReusableView")
_UICollectionViewListLayoutSectionBackgroundColorDecorationView = _Class(
    "_UICollectionViewListLayoutSectionBackgroundColorDecorationView"
)
_UICollectionViewListSwipeActionsView = _Class("_UICollectionViewListSwipeActionsView")
_UICollectionViewListHeaderFooter = _Class("_UICollectionViewListHeaderFooter")
_UICollectionViewListSeparatorView = _Class("_UICollectionViewListSeparatorView")
_UIContextMenuActionsListSeparatorView = _Class(
    "_UIContextMenuActionsListSeparatorView"
)
_UIContextMenuActionsListTitleView = _Class("_UIContextMenuActionsListTitleView")
_UICollectionSnapshotView = _Class("_UICollectionSnapshotView")
UIDebuggingInformationHierarchyLineView = _Class(
    "UIDebuggingInformationHierarchyLineView"
)
UIKeyboardEmojiSectionHeader = _Class("UIKeyboardEmojiSectionHeader")
UIKeyboardCandidatePocketShadow = _Class("UIKeyboardCandidatePocketShadow")
UICollectionViewTableSeparatorView = _Class("UICollectionViewTableSeparatorView")
UICollectionViewTableHeaderFooterView = _Class("UICollectionViewTableHeaderFooterView")
UICollectionViewCell = _Class("UICollectionViewCell")
_UIContextMenuActionsListCell = _Class("_UIContextMenuActionsListCell")
_UIContextMenuActionsListLoadingCell = _Class("_UIContextMenuActionsListLoadingCell")
_UIPrintPreviewPageCell = _Class("_UIPrintPreviewPageCell")
_UIDatePickerCalendarDayCell = _Class("_UIDatePickerCalendarDayCell")
_UIDatePickerCalendarTimeWheelCell = _Class("_UIDatePickerCalendarTimeWheelCell")
_UIHorizontalIndexTitleBarCell = _Class("_UIHorizontalIndexTitleBarCell")
_UIAlertControllerTextFieldViewCollectionCell = _Class(
    "_UIAlertControllerTextFieldViewCollectionCell"
)
UIDebuggingInformationHierarchyCell = _Class("UIDebuggingInformationHierarchyCell")
UITableViewIndexOverlaySelectionViewCollectionViewCell = _Class(
    "UITableViewIndexOverlaySelectionViewCollectionViewCell"
)
UIKeyCommandDiscoverabilityHUDViewCell = _Class(
    "UIKeyCommandDiscoverabilityHUDViewCell"
)
UIKeyboardEmojiCollectionViewCell = _Class("UIKeyboardEmojiCollectionViewCell")
UIKBRecentInputCell = _Class("UIKBRecentInputCell")
UICollectionViewTableCell = _Class("UICollectionViewTableCell")
UICollectionViewListCell = _Class("UICollectionViewListCell")
_UICollectionViewListCell = _Class("_UICollectionViewListCell")
_UICollectionViewOutlineCell = _Class("_UICollectionViewOutlineCell")
UIToolbar = _Class("UIToolbar")
UITabBar = _Class("UITabBar")
UITabBarCustomizeView = _Class("UITabBarCustomizeView")
UIKeyboardGlobeKeyIntroductionView = _Class("UIKeyboardGlobeKeyIntroductionView")
UILabel = _Class("UILabel")
_UITableViewHeaderFooterViewLabel = _Class("_UITableViewHeaderFooterViewLabel")
_UIStatusBarStringView = _Class("_UIStatusBarStringView")
_UIActivityIndicatorMessageLabel = _Class("_UIActivityIndicatorMessageLabel")
UIDateLabel = _Class("UIDateLabel")
UITextLabel = _Class("UITextLabel")
UITableViewCountView = _Class("UITableViewCountView")
UITableViewLabel = _Class("UITableViewLabel")
UISegmentLabel = _Class("UISegmentLabel")
UIButtonLabel = _Class("UIButtonLabel")
UITabBarButtonLabel = _Class("UITabBarButtonLabel")
UITextFieldLabel = _Class("UITextFieldLabel")
UITextFieldCenteredLabel = _Class("UITextFieldCenteredLabel")
UISearchBarTextFieldLabel = _Class("UISearchBarTextFieldLabel")
UISearchBar = _Class("UISearchBar")
UIImageView = _Class("UIImageView")
_UITextAttachmentImageView = _Class("_UITextAttachmentImageView")
_UITextAttachmentPlaceholderView = _Class("_UITextAttachmentPlaceholderView")
_UIDynamicCaretHelpLabel = _Class("_UIDynamicCaretHelpLabel")
_UIDynamicCaretNoContentView = _Class("_UIDynamicCaretNoContentView")
_UIStatusBarImageView = _Class("_UIStatusBarImageView")
_UIStatusBarActivityIconView = _Class("_UIStatusBarActivityIconView")
_UIStatusBarRadarView = _Class("_UIStatusBarRadarView")
_UIStatusBarFocusableImageView = _Class("_UIStatusBarFocusableImageView")
_UILegibilityImageView = _Class("_UILegibilityImageView")
_UIPageIndicatorView = _Class("_UIPageIndicatorView")
_UITextFieldImageBackgroundView = _Class("_UITextFieldImageBackgroundView")
_UISearchBarScopeBarBackground = _Class("_UISearchBarScopeBarBackground")
_UISearchBarShadowView = _Class("_UISearchBarShadowView")
_UIBarBackgroundCustomImageContainer = _Class("_UIBarBackgroundCustomImageContainer")
_UIListContentImageView = _Class("_UIListContentImageView")
_UIInterfaceActionImagePropertyView = _Class("_UIInterfaceActionImagePropertyView")
_UIShadowView = _Class("_UIShadowView")
_UIVerticalEdgeShadowView = _Class("_UIVerticalEdgeShadowView")
_UIRoundedRectShadowView = _Class("_UIRoundedRectShadowView")
_UICutoutShadowView = _Class("_UICutoutShadowView")
_UIVisualEffectImageView = _Class("_UIVisualEffectImageView")
_UIBarBackgroundShadowContentImageView = _Class(
    "_UIBarBackgroundShadowContentImageView"
)
UISelectionGrabberDot = _Class("UISelectionGrabberDot")
UIDynamicCaret = _Class("UIDynamicCaret")
UIKBCursorSelection = _Class("UIKBCursorSelection")
UISegment = _Class("UISegment")
UIMovieScrubberThumbnailView = _Class("UIMovieScrubberThumbnailView")
UITabBarSwappableImageView = _Class("UITabBarSwappableImageView")
_UIBarBackgroundImageView = _Class("_UIBarBackgroundImageView")
UISearchBarBackground = _Class("UISearchBarBackground")
UINavigationBarBackIndicatorView = _Class("UINavigationBarBackIndicatorView")
UINavigationBar = _Class("UINavigationBar")
UITutorialAnimatedView = _Class("UITutorialAnimatedView")
UITutorialFramingView = _Class("UITutorialFramingView")
UIVisualEffectView = _Class("UIVisualEffectView")
_UIPointerEffectTintView = _Class("_UIPointerEffectTintView")
_UIInteractiveHighlightBackgroundEffectView = _Class(
    "_UIInteractiveHighlightBackgroundEffectView"
)
_UIBarBackgroundShadowView = _Class("_UIBarBackgroundShadowView")
UIKBBackdropView = _Class("UIKBBackdropView")
UIKBVisualEffectView = _Class("UIKBVisualEffectView")
UIInterfaceActionRepresentationView = _Class("UIInterfaceActionRepresentationView")
_UIInterfaceActionSystemRepresentationView = _Class(
    "_UIInterfaceActionSystemRepresentationView"
)
_UIInterfaceActionCustomViewRepresentationView = _Class(
    "_UIInterfaceActionCustomViewRepresentationView"
)
UIInterfaceActionGroupView = _Class("UIInterfaceActionGroupView")
_UIAlertControllerInterfaceActionGroupView = _Class(
    "_UIAlertControllerInterfaceActionGroupView"
)
UIAlertView = _Class("UIAlertView")
_UIUserNotificationAlertView = _Class("_UIUserNotificationAlertView")
UIActionSheet = _Class("UIActionSheet")
UIWindow = _Class("UIWindow")
_UIContextMenuAnimationWindow = _Class("_UIContextMenuAnimationWindow")
_UIBannerWindow = _Class("_UIBannerWindow")
_UISnapshotWindow = _Class("_UISnapshotWindow")
_UIBackgroundHitTestWindow = _Class("_UIBackgroundHitTestWindow")
_UIKeyCommandDiscoverabilityHUDWindow = _Class("_UIKeyCommandDiscoverabilityHUDWindow")
_UIWindowSceneUserInterfaceStyleAnimationSnapshotWindow = _Class(
    "_UIWindowSceneUserInterfaceStyleAnimationSnapshotWindow"
)
_UIPreviewInteractionTransitionWindow = _Class("_UIPreviewInteractionTransitionWindow")
_UIInteractiveHighlightEffectWindow = _Class("_UIInteractiveHighlightEffectWindow")
_UIFeedbackVisualizerWindow = _Class("_UIFeedbackVisualizerWindow")
_UIDragSetDownAnimationWindow = _Class("_UIDragSetDownAnimationWindow")
_UIApplicationModalProgressWindow = _Class("_UIApplicationModalProgressWindow")
_UIWindowSceneAccessibilityContrastAnimationSnapshotWindow = _Class(
    "_UIWindowSceneAccessibilityContrastAnimationSnapshotWindow"
)
_UIHostedWindow = _Class("_UIHostedWindow")
_UISecureHostedWindow = _Class("_UISecureHostedWindow")
UIDebuggingInformationOverlay = _Class("UIDebuggingInformationOverlay")
UIStatusBarWindow = _Class("UIStatusBarWindow")
UIPrinterPickerWindow = _Class("UIPrinterPickerWindow")
UIPrintPanelWindow = _Class("UIPrintPanelWindow")
UISoftwareDimmingWindow = _Class("UISoftwareDimmingWindow")
_UIRootWindow = _Class("_UIRootWindow")
_UISystemGestureWindow = _Class("_UISystemGestureWindow")
UIRootSceneWindow = _Class("UIRootSceneWindow")
UIApplicationRotationFollowingWindow = _Class("UIApplicationRotationFollowingWindow")
_UIFallbackPresentationWindow = _Class("_UIFallbackPresentationWindow")
_UIAlertControllerShimPresenterWindow = _Class("_UIAlertControllerShimPresenterWindow")
UIAutoRotatingWindow = _Class("UIAutoRotatingWindow")
UITextEffectsWindow = _Class("UITextEffectsWindow")
UITextEffectsWindowHosted = _Class("UITextEffectsWindowHosted")
UIRemoteKeyboardWindow = _Class("UIRemoteKeyboardWindow")
UIRemoteKeyboardWindowHosted = _Class("UIRemoteKeyboardWindowHosted")
UIAccessibilityHUDWindow = _Class("UIAccessibilityHUDWindow")
UIAccessibilityHUDView = _Class("UIAccessibilityHUDView")
UIKBTutorialModalDisplay = _Class("UIKBTutorialModalDisplay")
UIKBEditingGesturesIntroduction = _Class("UIKBEditingGesturesIntroduction")
UIUndoTutorialView = _Class("UIUndoTutorialView")
UIContinuousPathIntroductionView = _Class("UIContinuousPathIntroductionView")
UIControl = _Class("UIControl")
_UIDatePickerIOSCompactView = _Class("_UIDatePickerIOSCompactView")
_UIDatePickerCalendarTimeWheel = _Class("_UIDatePickerCalendarTimeWheel")
_UICollectionViewListAccessoryDisclosure = _Class(
    "_UICollectionViewListAccessoryDisclosure"
)
_UICollectionViewListAccessoryControl = _Class("_UICollectionViewListAccessoryControl")
_UISearchDisplayControllerDimmingView = _Class("_UISearchDisplayControllerDimmingView")
_UICollectionViewListCellReorderControl = _Class(
    "_UICollectionViewListCellReorderControl"
)
_UIGrabber = _Class("_UIGrabber")
_UIActionSlider = _Class("_UIActionSlider")
_UIButtonBarButton = _Class("_UIButtonBarButton")
UIIndexBarView = _Class("UIIndexBarView")
UIIndexBarAccessoryView = _Class("UIIndexBarAccessoryView")
UIRemoveControl = _Class("UIRemoveControl")
UITableViewIndex = _Class("UITableViewIndex")
UITableViewCellReorderControl = _Class("UITableViewCellReorderControl")
UITableViewCellFocusableReorderControl = _Class(
    "UITableViewCellFocusableReorderControl"
)
UITableViewCellEditControl = _Class("UITableViewCellEditControl")
UITableViewCellFocusableEditControl = _Class("UITableViewCellFocusableEditControl")
UITableViewCellDetailDisclosureView = _Class("UITableViewCellDetailDisclosureView")
UIPrinterSetupPINView = _Class("UIPrinterSetupPINView")
UIDatePicker = _Class("UIDatePicker")
UICoverSheetButton = _Class("UICoverSheetButton")
UIKBUndoControl = _Class("UIKBUndoControl")
UIInputSwitcherSegmentControl = _Class("UIInputSwitcherSegmentControl")
UISwitch = _Class("UISwitch")
UIStepper = _Class("UIStepper")
UISlider = _Class("UISlider")
_UIPrototypingMenuSlider = _Class("_UIPrototypingMenuSlider")
_UIDynamicSlider = _Class("_UIDynamicSlider")
UISegmentedControl = _Class("UISegmentedControl")
UIRefreshControl = _Class("UIRefreshControl")
UIPageControl = _Class("UIPageControl")
UIMovieScrubber = _Class("UIMovieScrubber")
UITabBarButton = _Class("UITabBarButton")
UITextField = _Class("UITextField")
_UIAlertControllerTextField = _Class("_UIAlertControllerTextField")
UIDocumentPasswordField = _Class("UIDocumentPasswordField")
UISearchField = _Class("UISearchField")
UISearchTextField = _Class("UISearchTextField")
UISearchBarTextField = _Class("UISearchBarTextField")
UIToolbarButton = _Class("UIToolbarButton")
UIToolbarTextButton = _Class("UIToolbarTextButton")
UIButton = _Class("UIButton")
_UIStaticScrollbarButton = _Class("_UIStaticScrollbarButton")
_UIDatePickerTouchOutsetButton = _Class("_UIDatePickerTouchOutsetButton")
_UIStepperButton = _Class("_UIStepperButton")
_UITableViewCellActionButton = _Class("_UITableViewCellActionButton")
_UIStatusBarSystemNavigationItemButton = _Class(
    "_UIStatusBarSystemNavigationItemButton"
)
_UITextFieldClearButton = _Class("_UITextFieldClearButton")
_UIShortPlacardButton = _Class("_UIShortPlacardButton")
_UIPlacardButton = _Class("_UIPlacardButton")
_UITableCellAccessoryButton = _Class("_UITableCellAccessoryButton")
_UIModernBarButton = _Class("_UIModernBarButton")
UISwipeActionButton = _Class("UISwipeActionButton")
UISwipeActionStandardButton = _Class("UISwipeActionStandardButton")
UISwipeActionCircularButton = _Class("UISwipeActionCircularButton")
UIStatusBarCarPlayDockAppItemButton = _Class("UIStatusBarCarPlayDockAppItemButton")
UIAssistantBarRoundedButtonViewButton = _Class("UIAssistantBarRoundedButtonViewButton")
UIKeyboardDockItemButton = _Class("UIKeyboardDockItemButton")
UIKeyboardDictationStarkDoneButton = _Class("UIKeyboardDictationStarkDoneButton")
UIKeyboardButton = _Class("UIKeyboardButton")
UICalloutBarButton = _Class("UICalloutBarButton")
UISegmentAccessibilityButton = _Class("UISegmentAccessibilityButton")
UIPopoverButton = _Class("UIPopoverButton")
UITexturedButton = _Class("UITexturedButton")
UIRoundedRectButton = _Class("UIRoundedRectButton")
UIDictationSearchButton = _Class("UIDictationSearchButton")
UINavigationButton = _Class("UINavigationButton")
_UIToolbarNavigationButton = _Class("_UIToolbarNavigationButton")
UIColorWell = _Class("UIColorWell")
_UIColorWell = _Class("_UIColorWell")
UIViewController = _Class("UIViewController")
_UIPrototypingMenuViewController = _Class("_UIPrototypingMenuViewController")
_UIDatePickerIOSCompactViewController = _Class("_UIDatePickerIOSCompactViewController")
_UIContextMenuActionsOnlyViewController = _Class(
    "_UIContextMenuActionsOnlyViewController"
)
_UISearchControllerLimitedUIShieldViewController = _Class(
    "_UISearchControllerLimitedUIShieldViewController"
)
_UIAlternateApplicationIconsAlertContentViewController = _Class(
    "_UIAlternateApplicationIconsAlertContentViewController"
)
_UIScreenRoutePickerViewController = _Class("_UIScreenRoutePickerViewController")
_UIDatePickerNumericKeyboardViewController = _Class(
    "_UIDatePickerNumericKeyboardViewController"
)
_UINoDefinitionViewController = _Class("_UINoDefinitionViewController")
_UILongDefinitionViewController = _Class("_UILongDefinitionViewController")
_UIImagePickerPlaceholderViewController = _Class(
    "_UIImagePickerPlaceholderViewController"
)
_UIProgressiveBlurContextController = _Class("_UIProgressiveBlurContextController")
_UIButtonGroupViewController = _Class("_UIButtonGroupViewController")
_UIAlertViewShimAccessoryViewController = _Class(
    "_UIAlertViewShimAccessoryViewController"
)
_UIViewServiceViewControllerOperator = _Class("_UIViewServiceViewControllerOperator")
_UIWaitingForRemoteViewContainerViewController = _Class(
    "_UIWaitingForRemoteViewContainerViewController"
)
_UIResilientRemoteViewContainerViewController = _Class(
    "_UIResilientRemoteViewContainerViewController"
)
UIDocumentSharingController = _Class("UIDocumentSharingController")
_UISharingViewController = _Class("_UISharingViewController")
UICloudSharingController = _Class("UICloudSharingController")
UIPredictionViewController = _Class("UIPredictionViewController")
UIKeyboardPopoverController = _Class("UIKeyboardPopoverController")
UIDebuggingZoomViewController = _Class("UIDebuggingZoomViewController")
UIDebuggingSpecViewController = _Class("UIDebuggingSpecViewController")
UIDebuggingInformationVCHierarchyViewController = _Class(
    "UIDebuggingInformationVCHierarchyViewController"
)
UIDebuggingInformationVCDetailViewController = _Class(
    "UIDebuggingInformationVCDetailViewController"
)
UIDebuggingInformationOverlayWindowPickerViewController = _Class(
    "UIDebuggingInformationOverlayWindowPickerViewController"
)
UIDebuggingInformationInspectorDetailViewController = _Class(
    "UIDebuggingInformationInspectorDetailViewController"
)
UIDebuggingInformationHierarchyViewController = _Class(
    "UIDebuggingInformationHierarchyViewController"
)
UIDebuggingInformationOverlayViewController = _Class(
    "UIDebuggingInformationOverlayViewController"
)
UIDebuggingKBAutoFillViewController = _Class("UIDebuggingKBAutoFillViewController")
UIFontPickerViewController = _Class("UIFontPickerViewController")
UIEditingOverlayViewController = _Class("UIEditingOverlayViewController")
UISearchController = _Class("UISearchController")
UISearchContainerViewController = _Class("UISearchContainerViewController")
UIKeyCommandDiscoverabilityHUDViewController = _Class(
    "UIKeyCommandDiscoverabilityHUDViewController"
)
UIPrinterSetupPINViewController = _Class("UIPrinterSetupPINViewController")
UIPrinterSetupDisplayPINViewController = _Class(
    "UIPrinterSetupDisplayPINViewController"
)
UIPrinterPickerViewController = _Class("UIPrinterPickerViewController")
UIPrintRangeViewController = _Class("UIPrintRangeViewController")
UIKeyboardHiddenViewController = _Class("UIKeyboardHiddenViewController")
UIKeyboardHiddenViewController_ExternalCredential = _Class(
    "UIKeyboardHiddenViewController_ExternalCredential"
)
UIKeyboardHiddenViewController_Save = _Class("UIKeyboardHiddenViewController_Save")
UIKeyboardHiddenViewController_Autofill = _Class(
    "UIKeyboardHiddenViewController_Autofill"
)
UISystemKeyboardDockController = _Class("UISystemKeyboardDockController")
UICandidateViewController = _Class("UICandidateViewController")
UICompatibilityPredictiveViewController = _Class(
    "UICompatibilityPredictiveViewController"
)
UISystemInputViewController = _Class("UISystemInputViewController")
UIKBStackViewController = _Class("UIKBStackViewController")
UIKBSystemLayoutViewController = _Class("UIKBSystemLayoutViewController")
UIKBAutoFillTestViewController = _Class("UIKBAutoFillTestViewController")
UIKBAutoFillTestGroundTruthGenerationViewController = _Class(
    "UIKBAutoFillTestGroundTruthGenerationViewController"
)
_UIRemoteViewController = _Class("_UIRemoteViewController")
_UIShareInvitationRemoteViewController = _Class(
    "_UIShareInvitationRemoteViewController"
)
_UIColorPickerRemoteViewController = _Class("_UIColorPickerRemoteViewController")
_UIFontPickerRemoteViewController = _Class("_UIFontPickerRemoteViewController")
_UIRemoteInputViewController = _Class("_UIRemoteInputViewController")
_UIScreenRoutePickerRemoteViewController = _Class(
    "_UIScreenRoutePickerRemoteViewController"
)
_UIDocumentPickerRemoteViewController = _Class("_UIDocumentPickerRemoteViewController")
_UIDocumentPickerExtensionRemoteViewController = _Class(
    "_UIDocumentPickerExtensionRemoteViewController"
)
UIKeyboardMediaServiceRemoteViewController = _Class(
    "UIKeyboardMediaServiceRemoteViewController"
)
UIApplicationRotationFollowingController = _Class(
    "UIApplicationRotationFollowingController"
)
_UIFallbackPresentationViewController = _Class("_UIFallbackPresentationViewController")
UIApplicationRotationFollowingControllerNoTouches = _Class(
    "UIApplicationRotationFollowingControllerNoTouches"
)
UIInputWindowController = _Class("UIInputWindowController")
UIWebDateTimePopoverViewController = _Class("UIWebDateTimePopoverViewController")
UIWebFileUploadPanel = _Class("UIWebFileUploadPanel")
UIInputViewController = _Class("UIInputViewController")
UICompatibilityInputViewController = _Class("UICompatibilityInputViewController")
UISystemInputAssistantViewController = _Class("UISystemInputAssistantViewController")
UIUndoTutorialViewController = _Class("UIUndoTutorialViewController")
UIDocumentPickerViewController = _Class("UIDocumentPickerViewController")
UIDocumentMenuViewController = _Class("UIDocumentMenuViewController")
UIDocumentPickerExtensionViewController = _Class(
    "UIDocumentPickerExtensionViewController"
)
UIAccessibilityLargeTextSegmentedViewController = _Class(
    "UIAccessibilityLargeTextSegmentedViewController"
)
UITableViewController = _Class("UITableViewController")
_UIRemoteDictionaryViewController = _Class("_UIRemoteDictionaryViewController")
UIDebuggingIvarViewController = _Class("UIDebuggingIvarViewController")
UIDebuggingInformationListTableViewController = _Class(
    "UIDebuggingInformationListTableViewController"
)
UIDebuggingInformationRootTableViewController = _Class(
    "UIDebuggingInformationRootTableViewController"
)
UIPrintingProgressViewController = _Class("UIPrintingProgressViewController")
UIPrinterUtilityTableViewController = _Class("UIPrinterUtilityTableViewController")
UIPrinterSetupConfigureViewController = _Class("UIPrinterSetupConfigureViewController")
UIPrinterBrowserViewController = _Class("UIPrinterBrowserViewController")
UIPrintPaperViewController = _Class("UIPrintPaperViewController")
UIPrintPanelTableViewController = _Class("UIPrintPanelTableViewController")
UIPrintMoreOptionsTableViewController = _Class("UIPrintMoreOptionsTableViewController")
UIRecentsInputViewController = _Class("UIRecentsInputViewController")
UIExpandedBarItemsTableViewController = _Class("UIExpandedBarItemsTableViewController")
UIWebSelectTableViewController = _Class("UIWebSelectTableViewController")
UISplitViewController = _Class("UISplitViewController")
UIMultiColumnViewController = _Class("UIMultiColumnViewController")
UIReferenceLibraryViewController = _Class("UIReferenceLibraryViewController")
UIPageViewController = _Class("UIPageViewController")
UIPageController = _Class("UIPageController")
UISnapshotModalViewController = _Class("UISnapshotModalViewController")
UICollectionViewController = _Class("UICollectionViewController")
_UIAlertControllerTextFieldViewController = _Class(
    "_UIAlertControllerTextFieldViewController"
)
UIPrintPreviewViewController = _Class("UIPrintPreviewViewController")
UITabBarController = _Class("UITabBarController")
UINavigationController = _Class("UINavigationController")
_UIDictationPrivacySheetController = _Class("_UIDictationPrivacySheetController")
_UIDocumentPickerNavigationBridgeController = _Class(
    "_UIDocumentPickerNavigationBridgeController"
)
UIPrintPanelNavigationController = _Class("UIPrintPanelNavigationController")
UIVideoEditorController = _Class("UIVideoEditorController")
UIImagePickerController = _Class("UIImagePickerController")
UIMoreNavigationController = _Class("UIMoreNavigationController")
UIMoreListController = _Class("UIMoreListController")
UIColorPickerViewController = _Class("UIColorPickerViewController")
_UIColorPickerViewController = _Class("_UIColorPickerViewController")
UIAlertController = _Class("UIAlertController")
_UIRotatingAlertController = _Class("_UIRotatingAlertController")
UIWebRotatingAlertController = _Class("UIWebRotatingAlertController")
UIKBAlertController = _Class("UIKBAlertController")
UIInterfaceActionGroupViewController = _Class("UIInterfaceActionGroupViewController")
_UITextAttributeDictionary = _Class("_UITextAttributeDictionary")
_UITextAttributeDictionaryImplI = _Class("_UITextAttributeDictionaryImplI")
_UITextAttributeDictionaryImplM = _Class("_UITextAttributeDictionaryImplM")
_UIMutableTextAttributeDictionary = _Class("_UIMutableTextAttributeDictionary")
UITableViewVisibleCells = _Class("UITableViewVisibleCells")
NSTextSelection = _Class("NSTextSelection")
_NSTextAttachmentLayoutContext = _Class("_NSTextAttachmentLayoutContext")
NSRTFWriter = _Class("NSRTFWriter")
NSHTMLWriter = _Class("NSHTMLWriter")
NSSubstituteWebResource = _Class("NSSubstituteWebResource")
NSTextCorrectionMarkerRendering = _Class("NSTextCorrectionMarkerRendering")
NSRTFReader = _Class("NSRTFReader")
NSRTFReaderTableState = _Class("NSRTFReaderTableState")
NSTextAttachmentViewProvider = _Class("NSTextAttachmentViewProvider")
_NSTextViewportLayoutObserver = _Class("_NSTextViewportLayoutObserver")
NSTextViewportLayoutController = _Class("NSTextViewportLayoutController")
UIPointFIFO = _Class("UIPointFIFO")
UIQuadCurvePointFIFO = _Class("UIQuadCurvePointFIFO")
UIBoxcarFilterPointFIFO = _Class("UIBoxcarFilterPointFIFO")
_UIPointVector = _Class("_UIPointVector")
NSTextBlock = _Class("NSTextBlock")
NSTextTable = _Class("NSTextTable")
NSTextTableBlock = _Class("NSTextTableBlock")
NSTextBlockLayoutHelper = _Class("NSTextBlockLayoutHelper")
_NSTextRunStorage = _Class("_NSTextRunStorage")
NSTextList = _Class("NSTextList")
NSStringDrawingTextStorageSettings = _Class("NSStringDrawingTextStorageSettings")
NSTextContentManager = _Class("NSTextContentManager")
NSTextContentStorage = _Class("NSTextContentStorage")
NSTextLineFragment = _Class("NSTextLineFragment")
NSCountableTextLocation = _Class("NSCountableTextLocation")
NSTextRange = _Class("NSTextRange")
NSCountableTextRange = _Class("NSCountableTextRange")
NSLayoutManagerTextBlockRowArrayCache = _Class("NSLayoutManagerTextBlockRowArrayCache")
NSLayoutManagerTextBlockHelper = _Class("NSLayoutManagerTextBlockHelper")
NSTextElement = _Class("NSTextElement")
NSTextParagraph = _Class("NSTextParagraph")
NSGlyphInfo = _Class("NSGlyphInfo")
NSCTGlyphInfo = _Class("NSCTGlyphInfo")
NSCIDGlyphInfo = _Class("NSCIDGlyphInfo")
NSIdentityGlyphInfo = _Class("NSIdentityGlyphInfo")
NSGlyphNameGlyphInfo = _Class("NSGlyphNameGlyphInfo")
_NSAttributeRun = _Class("_NSAttributeRun")
_NSAttributes = _Class("_NSAttributes")
_NSCGTextGraphicsContext = _Class("_NSCGTextGraphicsContext")
UINibCoderValue = _Class("UINibCoderValue")
NSTextLayoutManager = _Class("NSTextLayoutManager")
NSTextSelectionNavigation = _Class("NSTextSelectionNavigation")
__NSTextSelectionLineFragmentInfo = _Class("__NSTextSelectionLineFragmentInfo")
NSLineFragmentRenderingContext = _Class("NSLineFragmentRenderingContext")
NSTextLayoutFragment = _Class("NSTextLayoutFragment")
NSHTMLWebDelegate = _Class("NSHTMLWebDelegate")
NSHTMLReader = _Class("NSHTMLReader")
NSTextAlternatives = _Class("NSTextAlternatives")
__NSTextAppearanceEffectContext = _Class("__NSTextAppearanceEffectContext")
_NSUIKitTextGraphicsContext = _Class("_NSUIKitTextGraphicsContext")
_NSStandardTextGraphicsContextProvider = _Class(
    "_NSStandardTextGraphicsContextProvider"
)
NSTextGraphicsContextProvider = _Class("NSTextGraphicsContextProvider")
NSTextAttachment = _Class("NSTextAttachment")
NSTextTab = _Class("NSTextTab")
NSDataAsset = _Class("NSDataAsset")
NSInsertionPointHelper = _Class("NSInsertionPointHelper")
_NSCoreTypesetterLayoutCache = _Class("_NSCoreTypesetterLayoutCache")
NSATSGlyphStorage = _Class("NSATSGlyphStorage")
NSATSLineFragment = _Class("NSATSLineFragment")
NSGlyphGenerator = _Class("NSGlyphGenerator")
_NSATSTypesetterGuts = _Class("_NSATSTypesetterGuts")
NSTextContainer = _Class("NSTextContainer")
NSParagraphArbitrator = _Class("NSParagraphArbitrator")
NSExtraLMData = _Class("NSExtraLMData")
NSRunStorage = _Class("NSRunStorage")
NSIdRunStorage = _Class("NSIdRunStorage")
NSStorage = _Class("NSStorage")
_NSTextStorageSideData = _Class("_NSTextStorageSideData")
UINibStringIDTable = _Class("UINibStringIDTable")
NSLayoutManager = _Class("NSLayoutManager")
NSTypesetter = _Class("NSTypesetter")
NSATSTypesetter = _Class("NSATSTypesetter")
NSSingleLineTypesetter = _Class("NSSingleLineTypesetter")
NSCoreTypesetter = _Class("NSCoreTypesetter")
NSStringDrawingContext = _Class("NSStringDrawingContext")
NSShadow = _Class("NSShadow")
NSParagraphStyleExtraData = _Class("NSParagraphStyleExtraData")
__NSFontExtraData = _Class("__NSFontExtraData")
UIFontDescriptor = _Class("UIFontDescriptor")
UICTFontDescriptor = _Class("UICTFontDescriptor")
_UIFontCacheKey = _Class("_UIFontCacheKey")
_UIFontDescriptorCacheKey = _Class("_UIFontDescriptorCacheKey")
_UIFontTextStyleCacheKey = _Class("_UIFontTextStyleCacheKey")
_UIFontNameCacheKey = _Class("_UIFontNameCacheKey")
_UIFontSystemCacheKey = _Class("_UIFontSystemCacheKey")
UIFont = _Class("UIFont")
NSFont = _Class("NSFont")
UICTFont = _Class("UICTFont")
_UICache = _Class("_UICache")
NSParagraphStyle = _Class("NSParagraphStyle")
NSMutableParagraphStyle = _Class("NSMutableParagraphStyle")
UINibEncoder = _Class("UINibEncoder")
UINibDecoder = _Class("UINibDecoder")
NSAttributeDictionaryEnumerator = _Class("NSAttributeDictionaryEnumerator")
_NSCachedAttributedString = _Class("_NSCachedAttributedString")
NSConcreteNotifyingMutableAttributedString = _Class(
    "NSConcreteNotifyingMutableAttributedString"
)
NSTextStorage = _Class("NSTextStorage")
__NSImmutableTextStorage = _Class("__NSImmutableTextStorage")
NSConcreteTextStorage = _Class("NSConcreteTextStorage")
NSStringDrawingTextStorage = _Class("NSStringDrawingTextStorage")
__NSATSStringSegment = _Class("__NSATSStringSegment")
NSAttributeDictionary = _Class("NSAttributeDictionary")
NSTempAttributeDictionary = _Class("NSTempAttributeDictionary")
