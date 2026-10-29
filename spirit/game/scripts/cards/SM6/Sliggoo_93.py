from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="607f914c-ef72-5d14-a622-55dd8ead3abe",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1", "Sliggoo"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
