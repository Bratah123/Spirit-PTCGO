from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    gathering_of_cats_passive,
)

card = PokemonCardDef(
    guid="175b7f6d-d24f-5ee6-8188-517d158fae07",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=148,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Gathering of Cats",
            game_text="Ignore all Energy in the attack costs of each of your Pok\u00e9mon in play that has the Caturday attack.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=gathering_of_cats_passive
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)