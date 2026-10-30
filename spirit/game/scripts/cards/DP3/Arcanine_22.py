"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp3_arcanine_22_flame_dash,
)
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(guid='ecd0e636-bb0b-5cca-963d-8ccfcbf894b5', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name', display_name='Arcanine', searchable_by=['Arcanine', 'Stage 1', 'Arcanine'], subtypes=['Stage 1'], collector_number=22, set_code='DP3', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name', family_id=58, abilities=[Ability(title='Flame Dash', game_text='Once during your turn, when you play Arcanine from your hand to evolve 1 of your Benched Pokémon, you may switch Arcanine with 1 of your Active Pokémon. If you do, you may move any number of Energy cards attached to that Pokémon to Arcanine.', ability_type=AbilityTypes.POKE_POWER, effect=dp3_arcanine_22_flame_dash(), activation=Activations.ONCE_PER_TURN), Attack(title='Inferno Onrush', game_text='Arcanine does 40 damage to itself.', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2}, damage=120, effect=recoil_attack(40, damage=120))])
