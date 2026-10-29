from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import super_electromagnetic_tackle

from spirit.game.card_effects.sm10 import (
    grand_flame,
)

card = PokemonCardDef(
    guid="6fd3b827-ae03-5b34-b6fd-c569485c076c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Grand Flame",
            game_text="Attach 2 Fire Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=120,
            effect=grand_flame
        ),
        Attack(
            title="Heat Tackle",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 4},
            damage=190,
            effect=super_electromagnetic_tackle,
        ),
    ],
)