"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import hyper_splash
from spirit.game.card_effects.ex import (
    driving_howl,
)

card = PokemonCardDef(guid='3d42e867-4928-5bf2-b0d7-d7254d303f3b', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mightyenaex.Name', display_name='Mightyena ex', searchable_by=['Mightyena ex', 'Stage 1', 'ex', 'Mightyenaex'], subtypes=['Stage 1', 'ex'], collector_number=101, set_code='EX13', rarity=Rarities.RareHoloEX, hp=100, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name', family_id=261, abilities=[Ability(title='Driving Howl', game_text="Once during your turn (before your attack), you may choose 1 of the Defending Pokémon and switch it with 1 of your opponent's Benched Pokémon. Your opponent chooses the Benched Pokémon to switch. This power can't be used if Mightyena ex is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=driving_howl(), activation=Activations.ONCE_PER_TURN), Attack(title='Sharp Fang', cost={PokemonTypes.COLORLESS: 2}, damage=30), Attack(title='Hyper Claws', game_text='If the Defending Pokémon is a Stage 2 Evolved Pokémon, this attack does 50 damage plus 40 more damage.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=50, damage_operator='+', effect=hyper_splash())])
