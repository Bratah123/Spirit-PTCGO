"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    granite_head,
    primal_light_search_basic,
)

card = PokemonCardDef(guid='cb1ec959-e0ec-5b10-855b-428fb092db92', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name', display_name='Aerodactyl δ', searchable_by=['Aerodactyl δ', 'Stage 1', 'Aerodactyl'], subtypes=['Stage 1'], collector_number=35, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name', family_id=142, abilities=[Ability(title='Primal Light', game_text="Once during your turn (before your attack), you may search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Aerodactyl is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=primal_light_search_basic(), activation=Activations.ONCE_PER_TURN), Attack(title='Granite Head', game_text="During your opponent's next turn, any damage done to Aerodactyl by attacks is reduced by 10 (after applying Weakness and Resistance).", cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=granite_head(10))])
