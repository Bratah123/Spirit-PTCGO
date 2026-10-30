from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import natural_cure_on_attach


card = PokemonCardDef(
    guid="fcafe523-c4cc-5d51-a046-0551b60467e5",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="When you attach a Grass Energy card from your hand to Grovyle, remove all Special Conditions from Grovyle.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=natural_cure_on_attach(PokemonTypes.GRASS),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
