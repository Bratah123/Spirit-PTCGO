from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    power_of_nature_passive,
    powerful_storm,
)

card = PokemonCardDef(
    guid="a8011617-270c-5286-ae8e-c0476ae677e8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=184,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Power of Nature",
            game_text="Prevent all damage done to your Pok\u00e9mon that have any Grass Energy attached to them by attacks from your opponent's Ultra Beasts.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=power_of_nature_passive,
        ),
        Attack(
            title="Powerful Storm",
            game_text="This attack does 20 damage times the amount of Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=powerful_storm,
        ),
    ],
)