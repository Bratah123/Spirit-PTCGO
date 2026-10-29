from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

from spirit.game.card_effects.sm9 import (
    electromagnetic_bomb,
)

card = PokemonCardDef(
    guid="14d44cd7-52c2-5dee-ae52-20dcae095fba",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2", "AlolanGolem"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Bomb",
            game_text="Move any number of Lightning Energy from your Benched Pok\u00e9mon to this Pok\u00e9mon. This attack does 20 damage for each Energy card you moved in this way.",
            cost={},
            damage=20,
            damage_operator="x",
            effect=electromagnetic_bomb,
        ),
        Attack(
            title="Super Zap Cannon",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 4},
            damage=190,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)