"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    hard_metal_may_recoil,
    heap_up_metal,
)

card = PokemonCardDef(guid='cdba22e3-6059-5d2b-a5bb-abc05eeaab55', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name', display_name='Aggron', searchable_by=['Aggron', 'Stage 2', 'Aggron'], subtypes=['Stage 2'], collector_number=1, set_code='DP2', rarity=Rarities.RareHolo, hp=130, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name', family_id=304, abilities=[Attack(title='Heap Up', game_text='Search your discard pile for all Energy cards and show them to your opponent. If you find any Metal Special Energy cards there this attack does 40 damage plus 30 more damage. Put all of those Energy cards on top of your deck. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=heap_up_metal(40, 30)), Attack(title='Hard Metal', game_text='You may do 60 damage plus 40 more damage. If you do, Aggron does 40 damage to itself.', cost={PokemonTypes.METAL: 4}, damage=60, damage_operator='+', effect=hard_metal_may_recoil(60, 40, 40))])
