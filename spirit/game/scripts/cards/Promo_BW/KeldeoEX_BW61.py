from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f2904028-46d6-5df9-af95-3a96a6e0831d",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoEX.Name",
    display_name="Keldeo-EX",
    searchable_by=["Keldeo-EX", "Basic", "EX", "KeldeoEX"],
    subtypes=["Basic", "EX"],
    collector_number=61,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=647,
    abilities=[
        Ability(
            title="Rush In",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Secret Sword",
            game_text="Does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)