from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import detect_flip_protect

card = PokemonCardDef(
    guid="4de79c57-e306-5115-9e05-a562285a4a5e",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Detect",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Grovyle during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
                        effect=detect_flip_protect(),
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)