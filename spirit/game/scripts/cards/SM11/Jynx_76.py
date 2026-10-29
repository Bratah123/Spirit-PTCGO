from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm11 import ominous_posture, ominous_posture_condition

card = PokemonCardDef(guid='e6372ae5-ad78-541b-b0ac-d0b8fddfb811', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name', display_name='Jynx', searchable_by=['Jynx', 'Basic', 'Jynx'], subtypes=['Basic'], collector_number=76, set_code='SM11', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=124, abilities=[Ability(title='Ominous Posture', game_text='Once during your turn (before your attack), you may move 1 damage counter from 1 of your Pokémon to another of your Pokémon.', ability_type=AbilityTypes.POKE_ABILITY, effect=ominous_posture, activation=Activations.ONCE_PER_TURN, condition=ominous_posture_condition), Attack(title='Attract Smack', game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=condition_attack(SpecialConditions.PARALYZED, flip=True))])
