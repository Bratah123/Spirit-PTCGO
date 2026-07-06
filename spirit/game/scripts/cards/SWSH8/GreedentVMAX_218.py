from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85df8316-8135-5eba-ada9-8fb201378dc6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentVMAX.Name",
    display_name="Greedent VMAX",
    searchable_by=["Greedent VMAX", "VMAX", "GreedentVMAX"],
    subtypes=["VMAX"],
    collector_number=218,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentV.Name",
    family_id=820,
    abilities=[
        Attack(
            title="Turn a Profit",
            game_text="If your opponent's Basic Pok\u00e9mon is Knocked Out by damage from this attack, take 2 more Prize cards.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Max Gimme Gimme",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)