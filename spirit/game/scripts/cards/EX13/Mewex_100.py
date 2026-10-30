"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    devo_crush,
    psychic_vision,
)

card = PokemonCardDef(guid='a6a77ad1-b951-5db3-a823-4ec7e482d237', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name', display_name='Mew ex', searchable_by=['Mew ex', 'Basic', 'ex', 'Mewex'], subtypes=['Basic', 'ex'], collector_number=100, set_code='EX13', rarity=Rarities.RareHoloEX, hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=151, abilities=[Ability(title='Psychic Vision', game_text="Once during your turn (before your attack), if Mew ex is on your Bench, you may look at your opponent's hand.", ability_type=AbilityTypes.POKE_POWER, effect=psychic_vision(), activation=Activations.ONCE_PER_TURN, usable_from='bench'), Attack(title='Super Psy Bolt', cost={PokemonTypes.COLORLESS: 2}, damage=30), Attack(title='Devo Crush', game_text="You may discard 2 Energy attached to Mew ex. If you do, you may remove the highest Stage Evolution card from the Defending Pokémon and shuffle that card into your opponent's deck.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=devo_crush())])
