from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm11 import trap_bolt

card = PokemonCardDef(guid='c8979410-3bf4-5cf0-a732-638a5a770edc', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name', display_name='Stunfisk', searchable_by=['Stunfisk', 'Basic', 'Stunfisk'], subtypes=['Basic'], collector_number=67, set_code='SM11', rarity=Rarities.Common, hp=90, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.METAL, resistance_amount=20, family_id=618, abilities=[Attack(title='Trap Bolt', game_text="If, before doing damage, your opponent's Active Pokémon has more remaining HP than this Pokémon, this attack does 30 more damage.", cost={PokemonTypes.FIGHTING: 1}, damage=30, damage_operator='+', effect=trap_bolt)])
