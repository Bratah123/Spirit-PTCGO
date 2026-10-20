from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import draw_until_effect


card = PokemonCardDef(
    guid="85990b1b-d62d-5ef1-81cd-8a2b4536b127",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Metal Blast",
            game_text="Does 20 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.METAL), 20, base=20),
        ),
        Attack(
            title="Lock Gear",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=draw_until_effect(6),
        ),
    ],
)