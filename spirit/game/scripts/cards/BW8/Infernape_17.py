from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6516ec40-c7af-5248-8bd7-ab7f0fe47933",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Team Plasma", "Infernape"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=17,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attack. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Malevolent Fire",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)