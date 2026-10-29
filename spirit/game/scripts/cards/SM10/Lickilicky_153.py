from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

from spirit.game.card_effects.sm10 import (
    eat_up,
)

card = PokemonCardDef(
    guid="35f0fba4-117b-5a06-b9d3-e6a687beb71b",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=153,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Eat Up",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards from your opponent's Active Pok\u00e9mon. If you discarded a Pok\u00e9mon Tool card in this way, heal all damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=eat_up
        ),
        Attack(
            title="Tonguenado",
            game_text="Flip 4 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=60),
        ),
    ],
)