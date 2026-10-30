from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import kerzap, paralyze_or_recoil


card = PokemonCardDef(
    guid="9e7965d2-f807-56de-9812-b5c24d5c41fa",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRaichu.Name",
    display_name="Lt. Surge's Raichu",
    searchable_by=["Lt. Surge's Raichu", "Stage 1", "LtSurgesRaichu"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesPikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Kerzap",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage to the Defending Pok\u00e9mon and discard all Lightning Energy cards attached to Lt. Surge's Raichu. If tails, this attack does 20 damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            damage_operator="+",
            effect=kerzap,
        ),
        Attack(
            title="Thundertackle",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, Lt. Surge's Raichu does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=paralyze_or_recoil(20),
        ),
    ],
)
