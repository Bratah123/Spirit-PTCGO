from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets

from spirit.game.card_effects.sm8 import (
    sympathetic_slap,
)

card = PokemonCardDef(
    guid="1f552055-5357-5b37-9547-dc846a46872d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Healing Pirouette",
            game_text="Heal 20 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(20, scope='each_own'),
        ),
        Attack(
            title="Sympathetic Slap",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it before this attack does damage, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=sympathetic_slap
        ),
    ],
)