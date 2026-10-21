from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack


card = PokemonCardDef(
    guid="7c686317-b01a-5d2f-b35f-d2eb846d08d7",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YanmegaBREAK.Name",
    display_name="Yanmega BREAK",
    searchable_by=["Yanmega BREAK", "BREAK", "YanmegaBREAK"],
    subtypes=["BREAK"],
    collector_number=8,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    family_id=193,
    abilities=[
        Attack(
            title="Barrier Break",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)