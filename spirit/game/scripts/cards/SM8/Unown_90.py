from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    unown_damage_condition,
    win_the_game,
)

card = PokemonCardDef(
    guid="ee460993-e56e-5255-90e1-d8454886dc55",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="DAMAGE",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, and if there are 66 or more damage counters on your Benched Pok\u00e9mon, you may use this Ability. If you do, you win this game.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=win_the_game,
            activation=Activations.ONCE_PER_TURN,
            condition=unown_damage_condition,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)