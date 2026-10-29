from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm11 import (
    injection_gx,
    ultra_conversion,
    ultra_conversion_condition,
    venom_shot,
)

card = PokemonCardDef(guid='0aa195f6-1db5-5f50-a34f-9a969c72f402', key='SM11', name='com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGX.Name', display_name='Naganadel-GX', searchable_by=['Naganadel-GX', 'Stage 1', 'GX', 'Ultra Beast', 'NaganadelGX'], subtypes=['Stage 1', 'GX', 'Ultra Beast'], collector_number=230, set_code='SM11', rarity=Rarities.RareUltra, hp=210, elements=[PokemonTypes.DRAGON], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FAIRY, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name', family_id=803, abilities=[Ability(title='Ultra Conversion', game_text='Once during your turn (before your attack), you may discard an Ultra Beast card from your hand. If you do, draw 3 cards.', ability_type=AbilityTypes.POKE_ABILITY, effect=ultra_conversion, activation=Activations.ONCE_PER_TURN, condition=ultra_conversion_condition), Attack(title='Venom Shot', game_text="Discard 2 Energy from this Pokémon. This attack does 170 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3}, effect=venom_shot), Attack(title='Injection-GX', game_text="Add a card from your opponent's discard pile to their Prize cards face down. (You can't use more than 1 GX attack in a game.)", cost={PokemonTypes.LIGHTNING: 1}, effect=injection_gx)])
