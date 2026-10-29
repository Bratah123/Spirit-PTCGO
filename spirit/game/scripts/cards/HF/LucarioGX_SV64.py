from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.card_effects.sm6 import aura_strike

card = PokemonCardDef(
    guid="34f9c7ff-a0ab-535b-b5b8-6e3dbf1c245c",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioGX.Name",
    display_name="Lucario-GX",
    searchable_by=["Lucario-GX", "Stage 1", "GX", "LucarioGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=133,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Aura Strike",
            game_text="If this Pok\u00e9mon evolved from Riolu during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=aura_strike,
        ),
        Attack(
            title="Cyclone Kick",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Cantankerous Beatdown-GX",
            game_text="This attack does 30 damage for each damage counter on this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 30),
        ),
    ],
)
