from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.session.effects import is_trainer_card


def _is_fusion_strike_trainer(card):
    return is_trainer_card(card) and "Fusion Strike" in subtypes_for(card.archetype_id)


sketching_trash = recover_from_discard(
    predicate=_is_fusion_strike_trainer, count=2, minimum=1, reveal=False, to="hand",
    prompt="Choose up to 2 Fusion Strike Trainer cards to put into your hand.",
)

card = PokemonCardDef(
    guid="5401114c-0180-51b0-a83b-8db481b1db3e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Fusion Strike", "Smeargle"],
    subtypes=["Basic", "Fusion Strike"],
    collector_number=209,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Attack(
            title="Sketching Trash",
            game_text="Put up to 2 Fusion Strike Trainer cards from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sketching_trash,
            condition=requires_discard(_is_fusion_strike_trainer),
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)