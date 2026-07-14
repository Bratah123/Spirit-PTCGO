from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="a9347ac2-89e4-55cd-bd60-47c258d25341",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="FlabÃ©bÃ©",
    searchable_by=["Flab\u00c3\u00a9b\u00c3\u00a9", "Basic", "Rapid Strike", "Flabb"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=71,
    set_code="SWSH7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)