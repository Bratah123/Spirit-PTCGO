from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm11 import dimension_breach

card = PokemonCardDef(guid='3a1ffcb1-952c-52a0-b8b1-0765f578e07c', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name', display_name='Giratina', searchable_by=['Giratina', 'Basic', 'Giratina'], subtypes=['Basic'], collector_number=86, set_code='SM11', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=487, abilities=[Ability(title='Dimension Breach', game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Special Energy from your opponent's Active Pokémon.", ability_type=AbilityTypes.POKE_ABILITY, effect=dimension_breach, trigger=Triggers.ON_PLAY), Attack(title='Fade to Black', game_text="Your opponent's Active Pokémon is now Confused.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=70, effect=condition_attack(SpecialConditions.CONFUSED))])
