from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="205a08f9-5a0d-5790-9e0f-3e4a6400e7c6",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureVMAX.Name",
    display_name="Chandelure VMAX",
    searchable_by=["Chandelure VMAX", "VMAX", "ChandelureVMAX"],
    subtypes=["VMAX"],
    collector_number=265,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureV.Name",
    family_id=609,
    abilities=[
        Ability(
            title="Cursed Shimmer",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon Tool cards from their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 70 damage for each Trainer card you find there.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)