"""DP4 Great Encounters — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp4_luvdisc_77_rendezvous,
    dp4_luvdisc_77_synchro_dance,
)

card = PokemonCardDef(guid='23781588-3c92-5423-8262-ee31ee73d701', key='DP4', name='com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name', display_name='Luvdisc', searchable_by=['Luvdisc', 'Basic', 'Luvdisc'], subtypes=['Basic'], collector_number=77, set_code='DP4', rarity=Rarities.Common, hp=60, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=370, abilities=[Attack(title='Rendezvous', game_text='Reveal the top card of your deck and put it into your hand. If that card is a Pokémon, draw 2 cards.', cost={PokemonTypes.COLORLESS: 1}, effect=dp4_luvdisc_77_rendezvous()), Attack(title='Synchro Dance', game_text='If Luvdisc and the Defending Pokémon have the same amount of Energy attached to them, this attack does 10 damage plus 20 more damage.', cost={PokemonTypes.WATER: 1}, damage=10, damage_operator='+', effect=dp4_luvdisc_77_synchro_dance())])
