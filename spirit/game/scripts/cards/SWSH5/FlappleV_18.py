from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import raise_defender_attack_cost_next_turn

card = PokemonCardDef(
    guid="438cc4c7-a3b8-5418-a12f-b4208ae66712",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlappleV.Name",
    display_name="Flapple V",
    searchable_by=["Flapple V", "Basic", "V", "FlappleV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=841,
    abilities=[
        Attack(
            title="Sour Spit",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks cost ColorlessColorless more.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=raise_defender_attack_cost_next_turn(extra=2),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)