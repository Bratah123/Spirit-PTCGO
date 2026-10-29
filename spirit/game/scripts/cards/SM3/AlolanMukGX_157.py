from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush
from spirit.game.card_effects.sm3 import chemical_breath, tri_hazard_gx

card = PokemonCardDef(
    guid="26e0fdbb-096b-57b8-9856-fec22f6827b4",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMukGX.Name",
    display_name="Alolan Muk-GX",
    searchable_by=["Alolan Muk-GX", "Stage 1", "GX", "AlolanMukGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=157,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Attack(
            title="Chemical Breath",
            game_text="This attack does 70 more damage for each Special Condition affecting your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=chemical_breath,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=rock_crush,
        ),
        Attack(
            title="Tri Hazard-GX",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Burned, Paralyzed, and Poisoned. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=tri_hazard_gx,
        ),
    ],
)
