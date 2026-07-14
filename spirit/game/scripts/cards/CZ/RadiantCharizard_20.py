from spirit.game.card_effects.pokemon import ExcitedHeartPassive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf1e9fc0-419d-5b88-b0ea-e6ab9b14ba3a",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantCharizard.Name",
    display_name="Radiant Charizard",
    searchable_by=["Radiant Charizard", "Basic", "Radiant", "RadiantCharizard"],
    subtypes=["Basic", "Radiant"],
    collector_number=20,
    set_code="CZ",
    rarity=Rarities.RareRadiant,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Ability(
            title="Excited Heart",
            game_text="This Pokémon's attacks cost Colorless less for each Prize card your opponent has taken.",
            passive=ExcitedHeartPassive(),
        ),
        Attack(
            title="Combustion Blast",
            game_text="During your next turn, this Pokémon can't use Combustion Blast.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 4},
            damage=250,
            locks_next_turn=True,
        ),
    ],
)
