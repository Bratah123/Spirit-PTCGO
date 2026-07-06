from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7632dddb-eb5d-5bb1-bb77-38c2649203e4",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Ability(
            title="Surprise Spores",
            game_text="During your opponent's turn, if this Pok\u00e9mon is discarded from your hand by an effect of an attack or Ability from your opponent's Pok\u00e9mon, or by an effect of your opponent's Item or Supporter cards, discard your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Hypno Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)