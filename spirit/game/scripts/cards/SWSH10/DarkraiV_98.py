from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="0387e604-211c-5d17-922c-b8395fd9cbb1",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiV.Name",
    display_name="Darkrai V",
    searchable_by=["Darkrai V", "Basic", "V", "DarkraiV"],
    subtypes=["Basic", "V"],
    collector_number=98,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Wind of Darkness",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Dark Void",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)