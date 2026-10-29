from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    underground_work_passive,
)

card = PokemonCardDef(
    guid="ddc7579d-839f-58e3-ba41-3267bea5d941",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Ability(
            title="Underground Work",
            game_text="If you discard this Pok\u00e9mon with the effect of Giovanni's Exile, discard the top card of your opponent's deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=underground_work_passive
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)