"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import shuffle_random_from_opponent_hand
from spirit.game.card_effects.dp import (
    dark_genes_passive,
)

card = PokemonCardDef(guid='88144272-b9a3-5341-861b-80aae1f558c0', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name', display_name='Honchkrow', searchable_by=['Honchkrow', 'Stage 1', 'Honchkrow'], subtypes=['Stage 1'], collector_number=10, set_code='DP2', rarity=Rarities.RareHolo, hp=90, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name', family_id=198, abilities=[Ability(title='Dark Genes', game_text="As long as Honchkrow has the Energy necessary to use its attack, each of your Murkrow can use Honchkrow's attack as its own without the Energy necessary to use that attack.", ability_type=AbilityTypes.POKE_BODY, passive=dark_genes_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Dark Wing Flaps', game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.", cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=shuffle_random_from_opponent_hand())])
