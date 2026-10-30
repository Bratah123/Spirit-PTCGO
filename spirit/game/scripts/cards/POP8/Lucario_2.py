"""Lucario (POP8 #2)."""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import brick_smash
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="5c0feabc-d38f-549e-8f83-dc1d81373d38",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="POP8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Blocking Punch",
            game_text="During your opponent's next turn, any damage done to Lucario by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Striking Kick",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=brick_smash(),
        ),
    ],
)
