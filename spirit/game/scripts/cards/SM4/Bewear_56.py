from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.card_effects.sm4 import fluffy_passive


card = PokemonCardDef(
    guid="d39573d3-372f-5739-a302-9eaa257cd1ba",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Ability(
            title="Fluffy",
            game_text="This Pok\u00e9mon takes 30 less damage from the attacks of your opponent's non-Fire Pok\u00e9mon (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=fluffy_passive,
        ),
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(active_is(is_evolution_pokemon), 60),
        ),
    ],
)