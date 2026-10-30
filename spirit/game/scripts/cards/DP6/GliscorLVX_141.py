"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp6_gliscorlvx_141_shoot_poison,
    switch_self_attack,
)

card = PokemonCardDef(guid='4bd62747-2043-502e-a5b7-8e081e3046c6', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.GliscorLVX.Name', display_name='Gliscor LV.X', searchable_by=['Gliscor LV.X', 'Level-Up', 'GliscorLVX'], subtypes=['Level-Up'], collector_number=141, set_code='DP6', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.LEVELUP, retreat_cost=0, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name', family_id=207, abilities=[Ability(title='Shoot Poison', game_text='Once during your turn (before your attack), when you put Gliscor LV.X from your hand onto your Active Gliscor, you may choose 1 of the Defending Pokémon. That Pokémon is now Paralyzed and Poisoned.', ability_type=AbilityTypes.POKE_POWER, effect=dp6_gliscorlvx_141_shoot_poison(), activation=Activations.ONCE_PER_TURN), Attack(title='Night Slash', game_text='You may switch Gliscor with 1 of your Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=60, effect=switch_self_attack(damage=60, optional=True))])
