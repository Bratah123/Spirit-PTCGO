from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, snipe_attack
from spirit.game.card_effects.ecard import opponent_has_benched


card = PokemonCardDef(
    guid="8eb834a7-26c5-57f3-a058-306a7b16b54e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGeodude.Name",
    display_name="Brock's Geodude",
    searchable_by=["Brock's Geodude", "Basic", "BrocksGeodude"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Lucky Shot",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon and flip a coin. If heads, this attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            condition=opponent_has_benched,
            effect=flip_or_nothing(then=snipe_attack(
                30, pool="bench",
                prompt="Choose 1 of your opponent's Benched Pokémon",
            )),
        ),
    ],
)
