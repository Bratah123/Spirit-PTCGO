"""STUB: effect not implemented — do not guess mechanics.
Bellossom (EX10 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import green_dance, full_bloom

card = PokemonCardDef(
    guid="9083ad7f-83bf-5f1a-ae59-b33b592ec5eb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2", "Bellossom"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Green Dance",
            game_text="Search your deck for up to 2 Grass Pok\u00e9mon, show them to your opponent, and put them into your hand. Shuffle your deck afterward. If you put any Grass Pok\u00e9mon into your hand, you may switch Bellossom with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=green_dance(2),
        ),
        Attack(
            title="Full Bloom",
            game_text="If you have at least 3 Bellossom in play, this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=full_bloom(50, 50, "Bellossom"),
        ),
    ],
)