from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import smug_face_passive, stalking_claws_gx

card = PokemonCardDef(
    guid="b86a08c8-78ab-5d3a-bd3e-d7b664a17d2b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanPersianGX.Name",
    display_name="Alolan Persian-GX",
    searchable_by=["Alolan Persian-GX", "Stage 1", "GX", "AlolanPersianGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=219,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Smug Face",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's TAG TEAM Pok\u00e9mon and Ultra Beasts, and by your opponent's Pok\u00e9mon that have any Special Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=smug_face_passive,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Stalking Claws-GX",
            game_text="This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=stalking_claws_gx,
        ),
    ],
)