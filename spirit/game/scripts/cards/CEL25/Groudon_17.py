from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_scaled_damage
from spirit.game.card_effects.support_common import is_energy

card = PokemonCardDef(
    guid="9affb786-a38e-5429-84b8-37ebec853940",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Magma Volcano",
            game_text="Discard the top 5 cards of your deck. This attack does 80 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=mill_scaled_damage(5, 80, pred=is_energy),
        ),
        Attack(
            title="Massive Rend",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)