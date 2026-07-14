from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_metal_energy_card

card = PokemonCardDef(
    guid="6d9455dc-f39f-57be-91dd-6080c6fac1c7",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    display_name="Origin Forme Dialga V",
    searchable_by=["Origin Forme Dialga V", "Basic", "V", "OriginFormeDialgaV"],
    subtypes=["Basic", "V"],
    collector_number=113,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Metal Coating",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(predicate=is_metal_energy_card, count=2, minimum=0),
        ),
        Attack(
            title="Temporal Rupture",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)