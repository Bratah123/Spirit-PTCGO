from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import lightning_burst


card = PokemonCardDef(
    guid="33d61250-af65-594c-8255-c0f4b1247bce",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Ability(
            title="Lightning Burst",
            game_text="Whenever you attach a Lightning Energy card from your hand to Raikou, if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. This power stops working while Raikou is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=lightning_burst,
        ),
        Attack(
            title="Lightning Tackle",
            game_text="Flip a coin. If tails, Raikou does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=50,
            effect=flip_damage(tails_self_damage=20),
        ),
    ],
)
