from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    conductive_body_passive,
)

card = PokemonCardDef(
    guid="f8410b8f-5584-5193-a075-c8f7e4392c84",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=374,
    abilities=[
        Ability(
            title="Conductive Body",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, its Retreat Cost is Colorless less for each Beldum on your Bench.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=conductive_body_passive,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)