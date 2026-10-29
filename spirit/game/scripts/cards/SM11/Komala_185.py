from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm11 import drowsing

card = PokemonCardDef(guid='f7a7836f-7834-5ec1-90fa-a1a6da71dc4c', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name', display_name='Komala', searchable_by=['Komala', 'Basic', 'Komala'], subtypes=['Basic'], collector_number=185, set_code='SM11', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=775, abilities=[Ability(title='Drowsing', game_text="If this Pokémon remains Asleep between turns, put 6 damage counters on your opponent's Active Pokémon.", ability_type=AbilityTypes.POKE_ABILITY, effect=drowsing, trigger=Triggers.BETWEEN_TURNS), Attack(title='Snooze', game_text='This Pokémon is now Asleep.', cost={PokemonTypes.COLORLESS: 1}, effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)))])
