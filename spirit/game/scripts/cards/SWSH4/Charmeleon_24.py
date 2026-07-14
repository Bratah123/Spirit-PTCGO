from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26def597-e505-5e7b-be27-8ad732154e23",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Raging Flames",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
            effect=mill_attack(3, opponent=False),
        ),
    ],
)