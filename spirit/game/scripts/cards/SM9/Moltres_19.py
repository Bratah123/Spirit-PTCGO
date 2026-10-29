from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

from spirit.game.card_effects.sm9 import (
    top_burner,
)

card = PokemonCardDef(
    guid="68ab8723-4359-5461-984f-0620fa67b7c2",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=146,
    abilities=[
        Attack(
            title="Top Burner",
            game_text="Discard all Fire Energy from this Pok\u00e9mon. Then, discard a card from the top of your opponent's deck for each Energy you discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            effect=top_burner,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)