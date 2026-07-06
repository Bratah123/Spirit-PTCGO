from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8fa1e990-b980-514c-8589-5c9a652d6ef9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChandelureVMAX.Name",
    display_name="Chandelure VMAX",
    searchable_by=["Chandelure VMAX", "VMAX", "ChandelureVMAX"],
    subtypes=["VMAX"],
    collector_number=40,
    set_code="SWSH8",
    rarity=Rarities.RareHoloVMAX,
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