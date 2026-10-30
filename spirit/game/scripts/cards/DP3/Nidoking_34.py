"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import (
    dp3_nidoking_34_pride_attack,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='8628e090-397f-55fd-9767-ca83560b6e10', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name', display_name='Nidoking', searchable_by=['Nidoking', 'Stage 2', 'Nidoking'], subtypes=['Stage 2'], collector_number=34, set_code='DP3', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name', family_id=32, abilities=[Attack(title='Poison Rub', game_text="The Defending Pokémon is now Poisoned. Before doing damage, you may switch 1 of the Defending Pokémon with 1 of your opponent's Benched Pokémon. The new Defending Pokémon is now Poisoned.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.POISONED)), Attack(title='Pride Attack', game_text='Flip a coin for each Nidoqueen on your Bench. This attack does 60 damage plus 30 more damage for each heads.', cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=dp3_nidoking_34_pride_attack())])
